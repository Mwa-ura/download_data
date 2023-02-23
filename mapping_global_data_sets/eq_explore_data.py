import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the file
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
	all_eq_data = json.load(f)

readable_data = 'data/readable_eq_data.json'
with open(readable_data, 'w') as f:
	json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))
# Extract magnitude data
"""
mags, logs, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
	
	log = eq_dict['geometry']['coordinates'][0]
	lat = eq_dict['geometry']['coordinates'][1]
	hover_text = eq_dict['properties']['title']
	mags.append(mag)
	logs.append(log)
	lats.append(lat)
	hover_texts.append(hover_text)
"""
mags = [mag['properties']['mag'] for mag in all_eq_dicts]
logs = [log['geometry']['coordinates'][0] for log in all_eq_dicts]
lats = [lat['geometry']['coordinates'][1] for lat in all_eq_dicts]
hover_texts = [hover_text['properties']['title'] for hover_text in all_eq_dicts]

# Map the earthquakes.
data = [{
	'type':'scattergeo',
	'lon':logs,
	'lat':lats,
	'text': hover_texts,
	'marker': {
		'size': [5*mag for mag in mags],
		'color': mags,
		'colorscale': 'Viridis',
		'reversescale': True,
		'colorbar': {'title':'Magnitude'}
		}
	}]
# Pull the metadata title
header_title = all_eq_data['metadata']['title']
print(header_title)
my_layout = Layout(title=header_title)
fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='global_earthquake.html')