try:

    import unittest
    import calc
    print("All Modules Loaded .. ")
except:
    print("Some Module are Missing !")


class TestCalc(unittest.TestCase):

    def test_add(self):
        """

        :return: Test Function for add
        """
        self.assertEqual(calc.madd(-1,1), 0)
        self.assertEqual(calc.madd(-1,-1), -2)
        self.assertEqual(calc.madd(1,1), 2)

    def test_divide(self):
        """

        :return: Test Function for Divide
        """
        self.assertEqual(calc.divide(5,2), 2.5)
        self.assertEqual(calc.divide(-1,1), -1)
        self.assertEqual(calc.divide(5,2), 2.5)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()