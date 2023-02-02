import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Open csv file
filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	# Print header and their index
	for index, column_header in enumerate(header_row):
			print(index, column_header) 
	
	# Get the date
	# Get the high temperture from the file
	# Get min temp from the data
	dates, high_temps, low_temps = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		high_temp = int(row[5])
		low_temp = int(row[6])
		dates.append(current_date)
		high_temps.append(high_temp)
		low_temps.append(low_temp)
 # print(high_temps)

# Plot the high temp
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, high_temps, c="red", alpha=0.5)
ax.plot(dates, low_temps, c="blue", alpha=0.5)

# Format graph
ax.set_title("Daily High and Low Temperatures - 2018", fontsize=18)
ax.set_xlabel("", fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("Temperatures (F)", fontsize=14)
# Fill color between high and low.
ax.fill_between(dates, high_temps, low_temps, facecolor='blue', alpha=0.1)
ax.tick_params(axis='both', which='major', labelsize=12)
plt.show()

