import os
import sqlite3
import requests
import json
from datetime import date, timedelta

dir_path = os.path.dirname(os.path.realpath(__file__))
db_filename = dir_path + '/zipCode_airQuality.db'
conn = sqlite3.connect(db_filename)
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS weather_info_data (zip_code TEXT, date_val TEXT, hour_gmt_val INTEGER, temperature REAL, relative_humidity INTEGER, precipitation REAL, cloud_cover INTEGER)")

open_meteo_url = "https://api.open-meteo.com/v1/forecast?"
params = {}
params["latitude"] = ""
params["longitude"] = ""
params["hourly"] = "temperature_2m,relative_humidity_2m,precipitation,cloud_cover"
params["temperature_unit"] = "fahrenheit"
params["past_days"] = 2
params["forecast_days"] = 1

date_yesterday = date.today() - timedelta(days = 1)

cur.execute("SELECT * FROM zip_code_to_coordinates")
coordinates = cur.fetchall()

for zip_code, latitude, longitude in coordinates:
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

        cur.execute("INSERT OR IGNORE INTO weather_info_data (zip_code, date_val, hour_gmt_val, temperature, relative_humidity, precipitation, cloud_cover) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (zip_code, date_yesterday, yesterday_timestamp_hour, yesterday_temperature, yesterday_relative_humidity, yesterday_precipitation, yesterday_cloud_cover))
conn.commit()

cur.close()
conn.close()