import unittest
from my_own_math  import CalculateNum

class TestForCalculation(unittest.TestCase):
    """test case"""
    def test_numbers_add(self):
        int_add = CalculateNum(1, 100)
        self.assertEqual(int_add, 101)

if __name__ == '__main__':
    unittest.main()