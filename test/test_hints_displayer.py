'''
Created on Jul 24, 2013

@author: Ana Salinas
'''
import unittest
import os
import sys
sys.path.append('../src/Player')

from Player.hint_displayer import HintsDisplayer

class TestHintsDisplayerClassAndMethods(unittest.TestCase):

    def setUp(self):
        self.game = ['4','0','0','0','0','1','6','5','0'],\
         ['0','0','7','0','4','0','0','0','1'],\
         ['0','5','0','8','0','6','0','0','3'],\
         ['5','4','8','0','3','0','9','7','0'],\
         ['0','0','0','0','0','4','0','0','8'],\
         ['1','0','0','7','0','0','2','0','0'],\
         ['0','7','0','0','0','0','0','0','4'],\
         ['0','0','0','2','0','0','0','6','0'],\
         ['6','0','5','0','1','0','3','0','0']
        self.hint = HintsDisplayer(self.game)
        self.lista = [1,2,3,4,5,6,7,8,9]
        
    def test_that_when_a_right_coordinate_is_set_the_right_value_is_returned(self):
        value = self.hint.get_value_in_cell("A2")
        self.assertEqual('2', value)
        
    def test_when_a_right_coordinate_is_set_a_number_from_1_to_9_is_returned(self):
        value = self.hint.get_value_in_cell("A2")
        self.assertTrue(self.is_number(value))
        
    def test_that_when_an_invalid_coordinate_is_set_an_error_is_displayed(self):
        value = self.hint.get_value_in_cell("A12")
        self.assertEqual('Error', value)
    
    def is_number(self, val):
        i = 0
        while i in range(len(self.lista)):
            if int(val) == self.lista[i]:
                return True
            else:
                i += 1
        return False
            
        

if __name__ == "__main__":
    unittest.main()