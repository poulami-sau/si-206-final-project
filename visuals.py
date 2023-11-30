import csv
import matplotlib
import matplotlib.pyplot as plt

avg_precipitation = []
avg_cloud_cover = []
avg_aqi = []

calculated_data = open("calculations.csv")
csv_file = csv.reader(calculated_data)

data = []
for row in csv_file:
    #row = tuple(row)
    data.append(row)

calculated_data.close()

num_data = []
for num in data[1:]:
    num[1] = float(num[1])
    num[2] = float(num[2])
    num[3] = float(num[3])
    num[4] = float(num[4])
    num[5] = int(num[5])
    updated = (num[0], num[1], num[2], num[3], num[4], num[5])
    num_data.append(updated)


def create_temperature_graph():
    sort_by_temperature = sorted(num_data, key = lambda x: x[1])

    top_10_temperature = []
    top_aqi = []
    for index in range(len(sort_by_temperature) - 10, len(sort_by_temperature)):
        top_10_temperature.append(sort_by_temperature[index][1])
        top_aqi.append(sort_by_temperature[index][5])

    fig1, ax1 = plt.subplots()
    ax1.scatter(top_10_temperature, top_aqi)
    ax1.set_xlabel("average temperature")
    ax1.set_ylabel("average aqi")
    ax1.set_title("Average AQI vs Top 10 Average Temperature (by State)")

    fig1.savefig("temperature.png")


def create_humidity_graph():
    sort_by_humidity = sorted(num_data, key = lambda x: x[2])

    top_10_humidity = []
    top_aqi = []
    for index in range(len(sort_by_humidity) - 10, len(sort_by_humidity)):
        top_10_humidity.append(sort_by_humidity[index][2])
        top_aqi.append(sort_by_humidity[index][5])

    fig2, ax2 = plt.subplots()
    ax2.scatter(top_10_humidity, top_aqi)
    ax2.set_xlabel("average relative_humidity")
    ax2.set_ylabel("average aqi")
    ax2.set_title("Average AQI vs Top 10 Average Relative Humidity (by State)")

    fig2.savefig("humidity.png")


def create_precipitation_graph():
    sort_by_precipitation = sorted(num_data, key = lambda x: x[3])

    top_10_precipitation = []
    top_aqi = []
    for index in range(len(sort_by_precipitation) - 10, len(sort_by_precipitation)):
        top_10_precipitation.append(sort_by_precipitation[index][3])
        top_aqi.append(sort_by_precipitation[index][5])

    fig3, ax3 = plt.subplots()
    ax3.scatter(top_10_precipitation, top_aqi)
    ax3.set_xlabel("average precipitation")
    ax3.set_ylabel("average aqi")
    ax3.set_title("Average AQI vs Top 10 Average Precipitation (by State)")

    fig3.savefig("precipitation.png")


def create_cloud_cover_graph():
    sort_by_cloud_cover = sorted(num_data, key = lambda x: x[4])

    top_10_cloud_cover = []
    top_aqi = []
    for index in range(len(sort_by_cloud_cover) - 10, len(sort_by_cloud_cover)):
        top_10_cloud_cover.append(sort_by_cloud_cover[index][4])
        top_aqi.append(sort_by_cloud_cover[index][5])

    fig4, ax4 = plt.subplots()
    ax4.scatter(top_10_cloud_cover, top_aqi)
    ax4.set_xlabel("average cloud cover")
    ax4.set_ylabel("average aqi")
    ax4.set_title("Average AQI vs Top 10 Average Cloud Cover (by State)")

    fig4.savefig("cloud_cover.png")


create_temperature_graph()
create_humidity_graph()
create_precipitation_graph()
create_cloud_cover_graph()
    