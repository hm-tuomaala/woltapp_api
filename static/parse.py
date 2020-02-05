import json

# Json data is loaded only once to the DATA variable once at the server startup
DATA = {}

# Load json data from restaurants.json
with open('static/restaurants.json') as restaurants:
    DATA = json.load(restaurants)
