import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x ** 3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='red', cmap=plt.cm.inferno, s=10)

# Set chart title & label axes.
ax.set_title("Cube numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
ax.axis([0, 5500, 0, 5500000])

plt.show()
