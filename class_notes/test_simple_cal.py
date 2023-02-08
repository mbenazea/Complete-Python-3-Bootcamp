# import the test modules
import unittest

import simple_calulation


class TestSimple_calulation(unittest.TestCase):
    
    def test_area_rec(self):
        Rec = simple_calulation.area_retangle(5,10)
        answer  = 50
        self.assertEqual(Rec, answer)

    def test_area_rec(self):
        
unittest.main()