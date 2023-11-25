import os
import sqlite3
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
db_filename = dir_path + '/zipCode_airQuality.db'
conn = sqlite3.connect(db_filename)
cur = conn.cursor()

cur.execute("SELECT state, AVG(temperature), AVG(relative_humidity), AVG(precipitation), AVG(cloud_cover) FROM weather_data JOIN zip_code_data ON weather_data.zip_code_id = zip_code_data.zip_code_id GROUP BY state")
results = cur.fetchall()

header_list = ["state", "avg_temperature", "avg_relative_humidity", "avg_precipitation", "avg_cloud_cover"]
fout = open("calculations.csv", "w")

writer = csv.writer(fout)
writer.writerow(header_list)

for state, avg_temperature, avg_relative_humidity, avg_precipitation, avg_cloud_cover in results:
    writer.writerow([state, round(avg_temperature, 2), round(avg_relative_humidity, 2), round(avg_precipitation, 5), round(avg_cloud_cover, 2)])

fout.close()

cur.close()
conn.close()