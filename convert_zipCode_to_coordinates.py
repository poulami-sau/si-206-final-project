import os
import sqlite3
import requests
import json
from config import GEOCODIO_KEY

dir_path = os.path.dirname(os.path.realpath(__file__))
db_filename = dir_path + '/zipCode_airQuality.db'
conn = sqlite3.connect(db_filename)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS zip_code_to_coordinates")
cur.execute("CREATE TABLE IF NOT EXISTS zip_code_to_coordinates (zip_code_id INTEGER, latitude REAL, longitude REAL, FOREIGN KEY (zip_code_id) REFERENCES zip_code_data(zip_code_id))")

geocodio_url = "https://api.geocod.io/v1.7/geocode?"
params = {}
params["api_key"] = GEOCODIO_KEY
params["postal_code"] = ""

cur.execute("SELECT zip_code_id, zip_code FROM zip_code_data")
zip_codes = cur.fetchall()

for zip_code in zip_codes:
    params["postal_code"] = zip_code[1]
    response = requests.get(geocodio_url, params=params)
    zip_code_info = json.loads(response.text)

    zip_code_latitude = zip_code_info["results"][0]["location"]["lat"]
    zip_code_longitude = zip_code_info["results"][0]["location"]["lng"]

    #print(zip_code[0], params["postal_code"], zip_code_latitude, zip_code_longitude)

    cur.execute("INSERT OR IGNORE INTO zip_code_to_coordinates (zip_code_id, latitude, longitude) VALUES (?, ?, ?)", (zip_code[0], zip_code_latitude, zip_code_longitude))

conn.commit()

cur.close()
conn.close()