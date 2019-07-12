import unittest
from unittest.mock import patch
from MyRequest.gold import Gold
import json


class Test_gold(unittest.TestCase):

    def test_gold(self):

        fake_json = [{"Soumil":'Ok'}]

        with patch('MyRequest.gold.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = fake_json

            obj = Gold()
            response = obj.get

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), fake_json)

if __name__ == "__main__":
    unittest.main()






