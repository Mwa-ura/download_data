import json

# Explore the structure of the file
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
	all_eq_data = json.load(f)

readable_data = 'data/readable_eq_data.json'
with open(readable_data, 'w') as f:
	json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))
# Extract magnitude data
mags, logs, lats = [], [], []
for eq_dict in all_eq_dicts:
	mag = eq_dict['properties']['mag']
	log = eq_dict['geometry']['coordinates'][0]
	lat = eq_dict['geometry']['coordinates'][1]
	mags.append(mag)
	logs.append(log)
	lats.append(lat)
print(mags[:10])
print(logs[:10])
print(lats[:10])