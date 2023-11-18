import os
import sqlite3
import requests
import json
from config import AIR_QUALITY_KEY
from datetime import date

dir_path = os.path.dirname(os.path.realpath(__file__))
db_filename = dir_path + '/zipCode_airQuality.db'
conn = sqlite3.connect(db_filename)
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS air_quality_data (zip_code TEXT, date_val TEXT, aqi INTEGER)")

cur.execute("SELECT * FROM zip_code_to_coordinates")
coordinates = cur.fetchall()
api_ninjas_url = "https://api.api-ninjas.com/v1/airquality?"
params = {}
params["X-Api-Key"] = AIR_QUALITY_KEY
params["lat"] = ""
params["lon"] = ""
for row in coordinates:
    zip = row[0]
    lat = row[1]
    lon = row[2]
    params["lat"] = lat
    params["lon"] = lon
    response = requests.get(api_ninjas_url, params=params)
    info = json.loads(response.text)
    aqi_num = info["overall_aqi"]
    date_today = date.today()
    cur.execute("INSERT OR IGNORE INTO air_quality_data (zip_code, date_val, aqi) VALUES (?, ?, ?)",
               (zip, date_today, aqi_num))
conn.commit()

cur.close()
conn.close()