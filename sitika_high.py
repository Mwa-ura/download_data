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
	dates, high_temps = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		high_temp = int(row[5])
		dates.append(current_date)
		high_temps.append(high_temp)
 # print(high_temps)

# Plot the high temp
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, high_temps, c="red")

# Format graph
ax.set_title("Sitka Daily High Temperatures", fontsize=18)
ax.set_xlabel("Date", fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("Temperatures (F)", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=12)
plt.show()

