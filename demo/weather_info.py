import os
import sqlite3
import requests
import json
from datetime import date, timedelta

def connect_database():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    db_filename = dir_path + '/demo.db'
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()

    return cur, conn

def fetch_yesterday_hourly_response_data(url, params):
    response = requests.get(url, params=params)
    response_data_info = json.loads(response.text)

    yesterday_hourly_list = response_data_info["hourly"]

    return yesterday_hourly_list

def insert_data(cur, conn, url, params):
    date_yesterday = date.today() - timedelta(days = 1)

    cur.execute("SELECT MAX(date_num) FROM weather_data")
    date_yesterday_id = cur.fetchone()[0]

    if date_yesterday_id == None:
        date_yesterday_id = 1

    cur.execute("SELECT MAX(zip_code_id), date_num FROM weather_data WHERE date_num = ?", (date_yesterday_id,))
    max_zip_code_id, current_date = cur.fetchone()

    if max_zip_code_id == None:
        max_zip_code_id = 1
    elif max_zip_code_id < 100:
        max_zip_code_id += 1
    elif max_zip_code_id == 100:
        cur.execute("SELECT date FROM dates WHERE day_id = ?", (date_yesterday_id,))
        yesterday_date_table_str = cur.fetchone()[0]

        if current_date != yesterday_date_table_str:
            max_zip_code_id = 1

            if date_yesterday_id < 7:
                date_yesterday_id += 1
            elif date_yesterday_id == 7:
                exit()
        else:
            exit()

    cur.execute("SELECT * FROM zip_code_to_coordinates where zip_code_id = ?", (max_zip_code_id,))
    zip_code_id, latitude, longitude = cur.fetchone()

    params["latitude"] = latitude
    params["longitude"] = longitude

    yesterday_info_list = fetch_yesterday_hourly_response_data(url, params)

    for hour in range(24):
        yesterday_timestamp = yesterday_info_list["time"][hour]
        yesterday_timestamp_hour = yesterday_timestamp[11:13]

        yesterday_temperature = yesterday_info_list["temperature_2m"][hour]
        yesterday_relative_humidity = yesterday_info_list["relative_humidity_2m"][hour]
        yesterday_precipitation = yesterday_info_list["precipitation"][hour]
        yesterday_cloud_cover = yesterday_info_list["cloud_cover"][hour]

        cur.execute("INSERT OR IGNORE INTO weather_data (zip_code_id, date_num, hour_gmt_val, temperature, relative_humidity, precipitation, cloud_cover) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (zip_code_id, date_yesterday, yesterday_timestamp_hour, yesterday_temperature, yesterday_relative_humidity, yesterday_precipitation, yesterday_cloud_cover))

    conn.commit()

# executed code
cur, conn = connect_database()

cur.execute("CREATE TABLE IF NOT EXISTS weather_data (zip_code_id INTEGER, date_num INTEGER, hour_gmt_val INTEGER, temperature REAL, relative_humidity INTEGER, precipitation REAL, cloud_cover INTEGER, FOREIGN KEY (zip_code_id) REFERENCES zip_code_data(zip_code_id))")

open_meteo_url = "https://api.open-meteo.com/v1/forecast?"
params = {}
params["latitude"] = ""
params["longitude"] = ""
params["hourly"] = "temperature_2m,relative_humidity_2m,precipitation,cloud_cover"
params["temperature_unit"] = "fahrenheit"
params["past_days"] = 2
params["forecast_days"] = 1

insert_data(cur, conn, open_meteo_url, params)

cur.close()
conn.close()