import os
import sqlite3
import requests
import json
from config import GEOCODIO_KEY

def connect_database():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    db_filename = dir_path + '/zipCode_airQuality.db'
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()

    return cur, conn

def fetch_zip_code_response_data(url, params):
    response = requests.get(url, params=params)
    response_data_info = json.loads(response.text)

    latitude = response_data_info["results"][0]["location"]["lat"]
    longitude = response_data_info["results"][0]["location"]["lng"]

    return latitude, longitude

def insert_data(cur, conn, url, params):
    cur.execute("SELECT MAX(zip_code_id) FROM zip_code_to_coordinates")
    max_zip_code_id = cur.fetchone()[0]

    if max_zip_code_id == None:
        max_zip_code_id = 1
    elif max_zip_code_id < 100:
        max_zip_code_id += 1
    elif max_zip_code_id == 100:
        exit()

    for zip_code_id in range(max_zip_code_id, max_zip_code_id + 25):
        cur.execute("SELECT zip_code FROM zip_code_data where zip_code_id = ?", (zip_code_id,))
        zip_code = cur.fetchone()[0]
        
        params["postal_code"] = zip_code

        zip_code_latitude, zip_code_longitude = fetch_zip_code_response_data(url, params)

        cur.execute("INSERT OR IGNORE INTO zip_code_to_coordinates (zip_code_id, latitude, longitude) VALUES (?, ?, ?)", (zip_code_id, zip_code_latitude, zip_code_longitude))
    
    conn.commit()




# executed code
cur, conn = connect_database()

cur.execute("CREATE TABLE IF NOT EXISTS zip_code_to_coordinates (zip_code_id INTEGER, latitude REAL, longitude REAL, FOREIGN KEY (zip_code_id) REFERENCES zip_code_data(zip_code_id))")

geocodio_url = "https://api.geocod.io/v1.7/geocode?"
params = {}
params["api_key"] = GEOCODIO_KEY
params["postal_code"] = ""

insert_data(cur, conn, geocodio_url, params)

cur.close()
conn.close()