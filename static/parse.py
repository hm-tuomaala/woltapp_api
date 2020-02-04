import json
import requests
import blurhash


def calculate_blurhash(url, components):
    image_response = requests.get(url, stream=True)
    hash = blurhash.encode(image_response.raw, x_components=components, y_components=components)
    return hash

def blurhashes_are_equal(calculated, marked_value):
    return calculated == marked_value

def validate_blurhashes(data):
    ret = []
    for item in data['restaurants']:
        marked_value = item['blurhash']

        # Compare calculated blurhashs to the marked values first with
        # x and y componont values of 4 because lenght of hashes are 36
        calculated = calculate_blurhash(item['image'], 4)

        if not blurhashes_are_equal(calculated, marked_value):
            ret.append(item)

    return ret



# Json data is loaded only once to the DATA variable once the server starts
DATA = {}

# Load json data from restaurants.json
with open('static/restaurants.json') as restaurants:
    DATA = json.load(restaurants)

# Restaurants with invalid blurhashes are stored in INVALID_HASHES
INVALID_HASHES = []

# Validating blurhash values
# NOTE: Calculating blurhashes is quite expensive so searching invalid blurhashes
# is commented for now:
# INVALID_HASHES = validate_blurhashes(DATA)
