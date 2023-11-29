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

def create_aq_table (date_today = date.today()):
    cur.execute("CREATE TABLE IF NOT EXISTS air_quality_data (zip_code_id INTEGER, date_num INTEGER, aqi INTEGER)")

    cur.execute("SELECT MAX(zip_code_id) FROM air_quality_data WHERE date_num = ?", (date_today,))
    max_zip_code_id = cur.fetchone()[0]

    if max_zip_code_id == None:
        max_zip_code_id = 1
    elif max_zip_code_id < 100:
        max_zip_code_id += 1
    elif max_zip_code_id == 100:
        exit()

    for i in range(max_zip_code_id, max_zip_code_id + 25):
        cur.execute("SELECT zip_code_id, latitude, longitude FROM zip_code_to_coordinates where zip_code_id = ?", (i,))
        zip_code_id, latitude, longitude = cur.fetchone()
            
        api_ninjas_url = "https://api.api-ninjas.com/v1/airquality?"
        params = {}
        params["X-Api-Key"] = AIR_QUALITY_KEY
        params["lat"] = ""
        params["lon"] = ""
        lat = latitude
        lon = longitude
        params["lat"] = lat
        params["lon"] = lon

        cur.execute("SELECT day FROM dates WHERE date = date_today")
        today_day = cur.fetchone()

        response = requests.get(api_ninjas_url, params=params)
        info = json.loads(response.text)
        aqi_num = info["overall_aqi"]
        cur.execute("INSERT OR IGNORE INTO air_quality_data (zip_code_id, date_num, aqi) VALUES (?, ?, ?)",
                    (zip_code_id, today_day, aqi_num))
        conn.commit()

    cur.close()
    conn.close()
