import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/significant_week.json'
with open(filename) as f:
    one_week_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(one_week_eq_data, f, indent=4)

one_week_eq_dicts = one_week_eq_data['features']

mags, lons, lats, titles = [], [], [], []
for eq_dict in one_week_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    titles.append(eq_dict['properties']['title'])

data = [
    {
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'marker': {
            'size': [3 * mag for mag in mags],
            'color': mags,
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {
                'title': 'Earthquake Magnitude'
            }
        }
    }
]

metadata_key = one_week_eq_data['metadata']
layout_title = metadata_key['title']
final_title = layout_title

my_layout = Layout(title=f"{final_title}")

fig = {
    'data': data,
    'layout': my_layout
}


offline.plot(fig, filename='one_week_global_earthquakes.html')
