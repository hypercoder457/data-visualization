import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates AND high temps, AND also low temps from this CSV file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)


# Plot the high & low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c = 'red', alpha = 0.5)
ax.plot(dates, lows, c = 'blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

# Format the temps plot.
title = f"Daily high and low temperatures -  \n2018({row[1]})" # Grab the station name from the CSV file for Sitka to auto generate a graph title.
plt.title(title, fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()