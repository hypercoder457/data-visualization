# Import the `csv` module
import csv
# Import matplotlib & datetime
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/2278891.csv'
# Open the file and alias it to the name `f`
with open(filename) as f:
    # Make an instance of a csv reader object
    reader = csv.reader(f)
    # This line of code will return the next object from the reader, aka the header rows in the CSV file
    header_row = next(reader)

    # Get the dates, high, & low temps from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        # Error checking code for if the high/low temp variables do not work, NOTE TO SELF(There is a HOLE in the CSV file for San Francisco.)
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            # If there is a `ValueError`, print a message that we are missing data for the current date.
            print(f"Missing data for {current_date}")
        else:
            # If this works successfully, then append the respective variables to there respective list.
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    # Print the index & column headers from the CSV file.
    print("Index and column headers are:")
    # NOTE, the `enumerate()` function will loop over the index & the column header simultaneously.
    # So that we can print the index & the column header at the same time.

    for index, column_header in enumerate(header_row):
        print(f"{index}, {column_header}")

# Plot the high/low temps for San Francisco.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.7)
ax.plot(dates, lows, c='blue', alpha=0.7)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)


# Format the plot, once again.
plot_title = "San Francisco Temperatures(high and low), 2018"
plt.title(plot_title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (Fahrenheit)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)


plt.show()
