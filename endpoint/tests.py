from django.test import TestCase
from static import parse
import requests
import blurhash

class TestJsonData(TestCase):

    def test_number_of_data_attributes(self):
        try:
            data = parse.DATA
        except AttributeError:
            self.skipTest("Json data not found")

        for item in data['restaurants']:
            self.assertEqual(len(item), 10)


    def test_required_attributes(self):
        try:
            data = parse.DATA
        except AttributeError:
            self.skipTest("Json data not found")

        required_keys = [
            "blurhash",
            "city",
            "currency",
            "delivery_price",
            "description",
            "image",
            "location",
            "name",
            "online",
            "tags"
            ]

        for item in data['restaurants']:
            keys = item.keys()
            self.assertEqual(required_keys, list(keys))

    def test_blurhash_length_is_even(self):
        try:
            data = parse.DATA
        except AttributeError:
            self.skipTest("Json data not found")

        for item in data['restaurants']:
            self.assertTrue(len(item['blurhash']) % 2 == 0)


    def test_blurhashes_values(self):
        try:
            data = parse.DATA
        except AttributeError:
            self.skipTest("Json data not found")

        for item in data['restaurants']:
            img = requests.get(item['image'], stream=True)
            hash = blurhash.encode(img.raw, x_components=4, y_components=4)
            self.assertEqual(item['blurhash'], hash)

class TestAPI(TestCase):

    def test_query_string_lenght_0_response(self):
        try:
            req = requests.get('http://localhost:8000/restaurants/search?q=&lat=60.17045&lon=24.93147')
        except requests.exceptions.ConnectionError:
            self.skipTest('Development server is not on')

        self.assertEqual(req.status_code, 400)

    def test_no_lat_value_response(self):
        try:
            req = requests.get('http://localhost:8000/restaurants/search?q=test&lat=&lon=24.93147')
        except requests.exceptions.ConnectionError:
            self.skipTest('Development server is not on')

        self.assertEqual(req.status_code, 400)

    def test_no_lon_value_response(self):
        try:
            req = requests.get('http://localhost:8000/restaurants/search?q=test&lat=60.17045&lon=')
        except requests.exceptions.ConnectionError:
            self.skipTest('Development server is not on')

        self.assertEqual(req.status_code, 400)

    def test_query_string_with_no_results(self):
        try:
            req = requests.get('http://localhost:8000/restaurants/search?q=test&lat=60.17045&lon=24.93147')
        except requests.exceptions.ConnectionError:
            self.skipTest('Development server is not on')

        right_response = {
            'restaurants': []
        }

        self.assertEqual(right_response, dict(req.json()))
