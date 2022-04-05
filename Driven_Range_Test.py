from Driven_Range import *
import unittest

class driven_range_test(unittest.TestCase):

    def test_rangeAndFrequency(self):
        self.assertTrue(driven_range().main([4,5]) == {'4-5': '2'})
    

unittest.main()