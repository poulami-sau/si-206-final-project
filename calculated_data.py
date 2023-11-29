import os
import sqlite3
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
db_filename = dir_path + '/zipCode_airQuality.db'
conn = sqlite3.connect(db_filename)
cur = conn.cursor()

cur.execute("CREATE TEMPORARY TABLE joined_weather_info AS SELECT state, AVG(temperature) AS avg_temperature, AVG(relative_humidity)" 
            "AS avg_relative_humidity, AVG(precipitation) AS avg_precipitation, AVG(cloud_cover) AS avg_cloud_cover FROM weather_data" 
            "JOIN zip_code_data ON weather_data.zip_code_id = zip_code_data.zip_code_id GROUP BY state")

cur.execute("CREATE TEMPORARY TABLE joined_aqi_info AS SELECT state, AVG(aqi) AS avg_aqi FROM air_quality_data JOIN zip_code_data"
            "ON air_quality_data.zip_code_id = zip_code_data.zip_code_id GROUP BY state")

cur.execute("SELECT joined_weather_info.state, avg_temperature, avg_relative_humidity, avg_precipitation, avg_cloud_cover,"
            "avg_aqi FROM joined_weather_info JOIN joined_aqi_info ON joined_weather_info.state = joined_aqi_info.state")
results = cur.fetchall()

header_list = ["state", "avg_temperature", "avg_relative_humidity", "avg_precipitation", "avg_cloud_cover", "avg_aqi"]
fout = open("calculations.csv", "w")

writer = csv.writer(fout)
writer.writerow(header_list)

for state, avg_temperature, avg_relative_humidity, avg_precipitation, avg_cloud_cover, avg_aqi in results:
    writer.writerow([state, round(avg_temperature, 2), round(avg_relative_humidity, 2), round(avg_precipitation, 5), round(avg_cloud_cover, 2), round(avg_aqi)])

fout.close()

cur.close()
conn.close()