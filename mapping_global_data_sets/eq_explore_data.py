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
mags = []
for eq_dict in all_eq_dicts:
	mag = eq_dict['properties']['mag']
	mags.append(mag)
print(mags[:10])