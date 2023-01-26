import csv

# Open csv file
filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	# Print header and their index
	""" for index, column_header in enumerate(header_row):
			print(index, column_header) 
	""" 

# Get the high temperture from the file
	high_temps = []
	for temp in reader:
		high_temp = int(temp[5])
		high_temps.append(high_temp)
print(high_temps)