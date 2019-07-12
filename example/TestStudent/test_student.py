import unittest
from student import Student


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setup class")

    @classmethod
    def tearDownClass(cls):
        print("Tear down class ")


    def setUp(self):
        print("function setup was ran ")
        self.std1 = Student(first="Soumil", last="Shah", language="Python")

    def tearDown(self):
        print("function tear down was ran ")

    def test_fullname(self):
        print("Function Test_fullname was Ran ")
        self.assertEqual(self.std1.fullname, 'Soumil-Shah')

    def test_email(self):
        print("Function Test_email was Ran ")
        self.assertEqual(self.std1.email, 'Soumil.Shah@company.com')

if __name__ == "__main__":
    unittest.main()