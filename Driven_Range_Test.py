from Driven_Range import *
import unittest

class driven_range_test(unittest.TestCase):
    def test_rangeAndFrequency(self):
        self.assertTrue(driven_range().processedOutput([4,5]) == {'4-5': '2'})
    
#if __name__ == "__main__":
#    driven_range_test().rangeAndFrequency()
unittest.main()