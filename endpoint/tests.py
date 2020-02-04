from django.test import TestCase
from static import parse
import requests
import blurhash

class TestJsonData(TestCase):

    def test_data_attributes(self):
        try:
            data = parse.DATA
        except AttributeError:
            self.skipTest("Json data not found")

        for item in parse.DATA['restaurants']:
            # try:
            #     hash = item["blurhash"]
            #     city = ["city"]
            #     currency = item["currency"]
            #     dp = item["delivery_price"]
            #     desc = item["description"]
            #     image = item["image"]
            #     location = item["location"]
            #     name = ["name"]
            #     online = item["online"]
            #     tags = item["tags"]
            # except KeyError:
            self.assertEqual(len(item), 10)


    def test_blurhashes(self):
        try:
            data = parse.DATA
        except AttributeError:
            self.skipTest("Json data not found")

        for item in parse.DATA['restaurants']:
            # Use x_components=3 and y_components=3
            if len(item['blurhash']) == 22:
                img = requests.get(item['image'], stream=True)
                hash = blurhash.encode(img.raw, x_components=3, y_components=3)
                self.assertEqual(item['blurhash'], hash)
            # Use x_components=4 and y_components=4
            elif len(item['blurhash']) == 36:
                img = requests.get(item['image'], stream=True)
                hash = blurhash.encode(img.raw, x_components=4, y_components=4)
                self.assertEqual(item['blurhash'], hash)
            # Else test that blurhash lenght is even
            else:
                hash_len = len(item['blurhash'])
                self.assertTrue(hash_len % 2 == 0)
