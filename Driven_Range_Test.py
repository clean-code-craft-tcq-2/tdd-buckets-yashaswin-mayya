from Driven_Range import *
import Driven_Range
import unittest

class driven_range_test(unittest.TestCase):

    def test_rangeAndFrequency(self):
        self.assertTrue(driven_range().main([4,5]) == {'4-5': '2'})
        self.assertTrue(driven_range().main([4,5,6,4]) == {'4-6': '4'})
        self.assertTrue(driven_range().main([1,2,3,4,5,6,7,9]) == {'1-7': '7', '9-9': '1'})
        self.assertTrue(driven_range().main([-3,-2,-1,1,2,3,4,6,7,8]) == {'-3--1': '3', '1-4': '4', '6-8': '3'})
        self.assertTrue(driven_range().main([3,3,5,4,10,11,12]) == {'3-5': '4', '10-12': '3'})
    
    def test_emptyInput(self):
        self.assertTrue(driven_range().main([]) == {})

    def test_a2dConvertion(self):
        self.assertTrue(driven_range().main(driven_range().convertAnalogToDigital([1000], '12Bits')) == {'2-2':'1'})
        self.assertTrue(driven_range().main(driven_range().convertAnalogToDigital([-1,4095], '12Bits')) == {})
        self.assertTrue(driven_range().main(driven_range().convertAnalogToDigital([1000], '10Bits')) == {'14-14':'1'})
        self.assertTrue(driven_range().main(driven_range().convertAnalogToDigital([-1,1024], '10Bits')) == {})
        self.assertTrue(driven_range().main(driven_range().convertAnalogToDigital([0], '10Bits')) == {'15-15': '1'})

        self.assertTrue(driven_range().main(driven_range().convertAnalogToDigital([0,500,1000,1500,2000,2500,3000,3500,4000], '12Bits')) == {'0-2':'3', '4-7': '4', '9-10': '2'})
        self.assertTrue(driven_range().main(driven_range().convertAnalogToDigital([0,250,500,750,1000], '10Bits')) == {'0-0':'1', '7-8': '2', '14-15': '2'})

unittest.main()