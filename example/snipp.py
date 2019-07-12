import unittest
from unittest.mock import patch
from MyRequest.gold import Gold


class Test_Gold(unittest.TestCase):
    def test_get(self):
        self.obj1 = Gold()

        with patch('gold.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Sucess"

            data = self.obj1.get
            self.assertEqual(data,'Sucess')


if __name__ == "__main__":
    unittest.main()



