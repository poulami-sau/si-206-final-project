import csv
import matplotlib
import matplotlib.pyplot as plt

avg_temperature = []
avg_relative_humidity = []
avg_precipitation = []
avg_cloud_cover = []
avg_aqi = []

calculated_data = open("calculations.csv")
csv_file = csv.reader(calculated_data)

next(csv_file)

for row in csv_file:
    avg_temperature.append(row[1])
    avg_relative_humidity.append(row[2])
    avg_precipitation.append(row[3])
    avg_cloud_cover.append(row[4])
    avg_aqi.append(row[5])

calculated_data.close()

fig1, ax1 = plt.subplots()
ax1.scatter(avg_temperature, avg_aqi)
ax1.set_xlabel("average temperature")
ax1.set_ylabel("average aqi")
ax1.set_title("Average AQI vs Average Temperature per State")

fig1.savefig("avg_aqi_vs_avg_temperature.png")

fig2, ax2 = plt.subplots()
ax2.scatter(avg_relative_humidity, avg_aqi)
ax2.set_xlabel("average relative_humidity")
ax2.set_ylabel("average aqi")
ax2.set_title("Average AQI vs Average Relative Humidity per State")

fig2.savefig("avg_aqi_vs_avg_relative_humidity.png")

fig3, ax3 = plt.subplots()
ax3.scatter(avg_precipitation, avg_aqi)
ax3.set_xlabel("average precipitation")
ax3.set_ylabel("average aqi")
ax3.set_title("Average AQI vs Average Precipitation per State")

fig3.savefig("avg_aqi_vs_avg_precipitation.png")

fig4, ax4 = plt.subplots()
ax4.scatter(avg_cloud_cover, avg_aqi)
ax4.set_xlabel("average cloud cover")
ax4.set_ylabel("average aqi")
ax4.set_title("Average AQI vs Average Cloud Cover per State")

fig4.savefig("avg_aqi_vs_avg_cloud_cover.png")
