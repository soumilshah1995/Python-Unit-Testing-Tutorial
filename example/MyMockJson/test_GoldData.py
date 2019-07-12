import unittest
from  unittest.mock import patch
from MyMockJson.GoldData import Gold


class TestGold(unittest.TestCase):

    def test_gold(self):
        fake_json = [{'Soumil':"Python"}]

        with patch('MyMockJson.GoldData.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = fake_json

            obj = Gold()
            response = obj.get

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), fake_json)


if __name__ == "__main__":
    unittest.main()

