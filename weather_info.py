import os
import sqlite3
import requests
import json
from datetime import date, timedelta

dir_path = os.path.dirname(os.path.realpath(__file__))
db_filename = dir_path + '/zipCode_airQuality.db'
conn = sqlite3.connect(db_filename)
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS weather_data (zip_code_id INTEGER, date_num INTEGER, hour_gmt_val INTEGER, temperature REAL, relative_humidity INTEGER, precipitation REAL, cloud_cover INTEGER, FOREIGN KEY (zip_code_id) REFERENCES zip_code_data(zip_code_id))")

open_meteo_url = "https://api.open-meteo.com/v1/forecast?"
params = {}
params["latitude"] = ""
params["longitude"] = ""
params["hourly"] = "temperature_2m,relative_humidity_2m,precipitation,cloud_cover"
params["temperature_unit"] = "fahrenheit"
params["past_days"] = 2
params["forecast_days"] = 1

cur.execute("SELECT MAX(date_num) FROM weather_data")
date_yesterday = cur.fetchone()[0]

cur.execute("SELECT MAX(zip_code_id) FROM weather_data WHERE date_val = ?", (date_yesterday,))
max_zip_code_id = cur.fetchone()[0]

if max_zip_code_id == None:
    max_zip_code_id = 1
elif max_zip_code_id < 100:
    max_zip_code_id += 1
elif max_zip_code_id == 100:
    exit()

cur.execute("SELECT * FROM zip_code_to_coordinates where zip_code_id = ?", (max_zip_code_id,))
zip_code_id, latitude, longitude = cur.fetchone()

params["latitude"] = latitude
params["longitude"] = longitude
response = requests.get(open_meteo_url, params=params)
weather_info = json.loads(response.text)

yesterday_info_list = weather_info["hourly"]

for hour in range(24):
    yesterday_timestamp = yesterday_info_list["time"][hour]
    yesterday_timestamp_hour = yesterday_timestamp[11:13]

    yesterday_temperature = yesterday_info_list["temperature_2m"][hour]
    yesterday_relative_humidity = yesterday_info_list["relative_humidity_2m"][hour]
    yesterday_precipitation = yesterday_info_list["precipitation"][hour]
    yesterday_cloud_cover = yesterday_info_list["cloud_cover"][hour]

    cur.execute("INSERT OR IGNORE INTO weather_data (zip_code_id, date_val, hour_gmt_val, temperature, relative_humidity, precipitation, cloud_cover) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (zip_code_id, date_yesterday, yesterday_timestamp_hour, yesterday_temperature, yesterday_relative_humidity, yesterday_precipitation, yesterday_cloud_cover))

conn.commit()

cur.close()
conn.close()