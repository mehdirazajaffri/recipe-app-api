from django.test import TestCase

from app.calc import add, subtract

class CalcTest(TestCase):
    
    def test_add_number(self):
        """Two numbers are added together"""
        self.assertEqual(add(3,8), 11)
        self.assertEqual(add(0,0), 0)
        self.assertEqual(add(-1,1), 0)
        self.assertEqual(add(-1,-1), -2)
        self.assertEqual(add(1,1), 2)
    
    def test_substract_numbers(self):
        """Values are substracted and returned"""
        self.assertEqual(subtract(5,11), 6)