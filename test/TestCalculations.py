import sys
import unittest
sys.path.append('D:\\python\\Python_310\\')
from src.Calculations import Calculations


class TestCalculations(unittest.TestCase):
    
    def test_sum(self):
        calculation=Calculations(8,2)
        self.assertEqual(calculation.get_sum(),10,'This is wrong.')
        
    def test_diff(self):
        calculation=Calculations(8,2)
        self.assertAlmostEqual(calculation.get_diff(),round(5.9),'This is wrong')
        
    #def test_print_string("Hello Balakrishna"):
        
        
        
        
if __name__== '__main__':
    unittest.main()