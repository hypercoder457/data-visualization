import csv

from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get the average rainfall from this file.
    dates, rainfall = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        rain_amount = float(row[3])
        rainfall.append(rain_amount)
        dates.append(current_date)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

# Plot the rainfall.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, c='red')

# Format the plot
plt.title("Rainfall for every 2 days - 2018(Sitka, Alaska)", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
