import json
import requests
import blurhash


def calculate_blurhash(url):
    image_response = requests.get(url, stream=True)
    hash = blurhash.encode(image_response.raw, x_components=3, y_components=3)
    return hash

def blurhashes_are_equal(calculated, marked_value):
    return calculated == marked_value

def validate_blurhashes(data):
    ret = []
    for item in data['restaurants']:
        calculated = calculate_blurhash(item['image'])
        marked_value = item['blurhash']
        if not blurhashes_are_equal(calculated, marked_value):
            ret.append(item)
    return ret



# Json data is loaded only once to the DATA variable once the server starts
# and restaurants with invalid blurhashes are stored in INVALID_HASHES
DATA = {}
INVALID_HASHES = []

with open('static/restaurants.json') as restaurants:
    DATA = json.load(restaurants)

# Validating blurhash values
# NOTE: Calculating blurhashes is quite expensive
INVALID_HASHES = validate_blurhashes(DATA)
