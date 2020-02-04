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
            

    def test_blurhashes_x_and_y_components_4(self):
        try:
            data = parse.DATA
        except AttributeError:
            self.skipTest("Json data not found")

        for item in data['restaurants']:
            img = requests.get(item['image'], stream=True)
            hash = blurhash.encode(img.raw, x_components=4, y_components=4)
            self.assertEqual(item['blurhash'], hash)
