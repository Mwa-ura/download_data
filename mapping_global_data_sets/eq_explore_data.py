import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

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
mags, logs, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
	mag = eq_dict['properties']['mag']
	log = eq_dict['geometry']['coordinates'][0]
	lat = eq_dict['geometry']['coordinates'][1]
	hover_text = eq_dict['properties']['title']
	mags.append(mag)
	logs.append(log)
	lats.append(lat)
	hover_texts.append(hover_text)
# print(mags[:10])
# print(logs[:10])
# print(lats[:10])

# Map the earthquakes.
data = [{
	'type':'scattergeo',
	'lon':logs,
	'lat':lats,
	'text': hover_text,
	'marker': {
		'size': [5*mag for mag in mags],
		'color': mags,
		'colorscale': 'Viridis',
		'reversescale': True,
		'colorbar': {'title':'Magnitude'}
		}
	}]
my_layout = Layout(title="Global Earthquakes")
fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='global_earthquake.html')