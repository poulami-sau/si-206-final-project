import os
import sqlite3
import requests
import json
from config import AIR_QUALITY_KEY
from datetime import date


def connect_database():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    db_filename = dir_path + '/zipCode_airQuality.db'
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()

    return cur, conn


def create_aq_table (cur, conn, date_today):
    cur.execute("SELECT COUNT(*) FROM air_quality_data JOIN dates ON air_quality_data.date_num = dates.day_id WHERE dates.date = ?", (date_today,))
    max_zip_code_id = cur.fetchone()[0]

    if max_zip_code_id == 0:
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

        cur.execute("SELECT day_id FROM dates WHERE date = ?", (date_today,))
        today_day = cur.fetchone()[0]

        response = requests.get(api_ninjas_url, params=params)
        info = json.loads(response.text)
        aqi_num = info["overall_aqi"]
        cur.execute("INSERT OR IGNORE INTO air_quality_data (zip_code_id, date_num, aqi) VALUES (?, ?, ?)",
                    (zip_code_id, today_day, aqi_num))
    conn.commit()


cur, conn = connect_database()
cur.execute("CREATE TABLE IF NOT EXISTS air_quality_data (zip_code_id INTEGER, date_num INTEGER, aqi INTEGER)")
create_aq_table(cur, conn, date_today = date.today())
cur.close()
conn.close()
