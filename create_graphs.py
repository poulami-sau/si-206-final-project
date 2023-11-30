import csv
import matplotlib.pyplot as plt
import numpy as np

def create_attribute_lists():
    avg_weekly_temperature = []
    avg_weekly_relative_humidity = []
    avg_weekly_precipitation = []
    avg_weekly_cloud_cover = []
    avg_weekly_aqi = []

    calculated_data = open("calculations.csv")
    csv_file = csv.reader(calculated_data)

    next(csv_file)

    for row in csv_file:
        avg_weekly_temperature.append(row[1])
        avg_weekly_relative_humidity.append(row[2])
        avg_weekly_precipitation.append(row[3])
        avg_weekly_cloud_cover.append(row[4])
        avg_weekly_aqi.append(row[5])

    calculated_data.close()

    avg_weekly_temperature = np.array(avg_weekly_temperature, dtype=float)
    avg_weekly_relative_humidity = np.array(avg_weekly_relative_humidity, dtype=float)
    avg_weekly_precipitation = np.array(avg_weekly_precipitation, dtype=float)
    avg_weekly_cloud_cover = np.array(avg_weekly_cloud_cover, dtype=float)
    avg_weekly_aqi = np.array(avg_weekly_aqi, dtype=float)

    return avg_weekly_temperature, avg_weekly_relative_humidity, avg_weekly_precipitation, avg_weekly_cloud_cover, avg_weekly_aqi

def create_and_save_visualization(fig, ax, list1, list2, ha_val, va_val, ha_direction, va_direction, xlabel, ylabel, title, filename):
    fig, ax = plt.subplots()

    correlation_coefficient = np.round(np.corrcoef(list1, list2)[0, 1], 2)
    ax.scatter(list1, list2)
    ax.text(ha_val, va_val, f'Correlation Coefficient: {correlation_coefficient}', ha=ha_direction, va=va_direction, fontsize=9)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    fig.savefig(filename)





# executed code
avg_weekly_temperature, avg_weekly_relative_humidity, avg_weekly_precipitation, avg_weekly_cloud_cover, avg_weekly_aqi = create_attribute_lists()

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()
fig4, ax4 = plt.subplots()

create_and_save_visualization(fig1, ax1, avg_weekly_temperature, avg_weekly_aqi, min(avg_weekly_temperature), max(avg_weekly_aqi), "left", "top", "Average Weekly Temperature", "Average Weekly AQI", "Average Weekly AQI vs Average Weekly Temperature per State", "avg_weekly_aqi_vs_avg_weekly_temperature.png")
create_and_save_visualization(fig2, ax2, avg_weekly_relative_humidity, avg_weekly_aqi, min(avg_weekly_relative_humidity), min(avg_weekly_aqi), "left", "bottom", "Average Weekly Relative Humidity", "Average Weekly AQI", "Average Weekly AQI vs Average Weekly Relative Humidity per State", "avg_weekly_aqi_vs_avg_weekly_relative_humidity.png")
create_and_save_visualization(fig3, ax3, avg_weekly_precipitation, avg_weekly_aqi, max(avg_weekly_precipitation), max(avg_weekly_aqi), "right", "top", "Average Weekly Precipitation", "Average Weekly AQI", "Average Weekly AQI vs Average Weekly Precipitation per State", "avg_weekly_aqi_vs_avg_weekly_precipitation.png")
create_and_save_visualization(fig4, ax4, avg_weekly_cloud_cover, avg_weekly_aqi, min(avg_weekly_cloud_cover), min(avg_weekly_aqi), "left", "bottom", "Average Weekly Cloud Cover", "Average Weekly AQI", "Average Weekly AQI vs Average Weekly Cloud Cover per State", "avg_weekly_aqi_vs_avg_weekly_cloud_cover.png")