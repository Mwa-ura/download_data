import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = "data/death_valley_2018_simple.csv"
with open(filename) as f:
	reader = csv.reader(f)
	header = next(reader)
	# Iterate the header
	for index in header:
		print(len(index))
	# Explore Dates, High & Low temps.
	dates, highs, lows = [], [], []
	for row in reader:
		date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			high = int(row[4])
			low = int(row[5])
		except ValueError:
			print(f"Missing value of date: {date}")
		else:
			dates.append(date)
			highs.append(high)
			lows.append(low)

#Plot the data
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="blue", alpha=0.5)

# Format the graph
ax.set_title("Daily High and Low Temperature - 2018", fontsize=16)
ax.set_xlabel("")
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=14)
ax.fill_between(dates, highs, lows, facecolor="aquamarine", alpha=0.7)
ax.tick_params(axis="both", which="major", labelsize=12)
plt.show()
