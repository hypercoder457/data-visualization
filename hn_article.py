import requests
import json

# Make an API call & store response.
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'

r = requests.get(url)
print(f"The request status code is {r.status_code}")

# Explore the structure of the JSON object returned from the API call.
response_dict = r.json()
readable_file = 'data/readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)
