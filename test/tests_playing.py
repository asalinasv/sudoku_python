#-------------------------------------------------------------------------------
# Name:        tests_playing
# Purpose:     validate playing_sudoku module
# Author:      Israel Azurduy
# Email:       israel.azurduy@gmail.com
# Created:     19/07/2013
# Copyright:   (c) Israel Azurduy 2013
#-------------------------------------------------------------------------------
import unittest
import copy
import sys
sys.path.append('../src')
from solver.sudokubacktrack import *
from Player.playing_sudoku import Game
from Player.playing_sudoku import MenuPlay


class TestPlaying(unittest.TestCase):

    def setUp(self):



        self.default_matrx= \
        [4,0,0,0,0,0,8,0,5], \
        [0,3,0,0,0,0,0,0,0], \
        [0,0,0,7,0,0,0,0,0], \
        [0,2,0,0,0,0,0,6,0], \
        [0,0,0,0,8,0,4,0,0], \
        [0,0,0,0,1,0,0,0,0], \
        [0,0,0,6,0,3,0,7,0], \
        [5,0,0,2,0,0,0,0,0], \
        [1,0,4,0,0,0,0,0,0]

        self.first_matrx= \
        [0,0,3,0,2,0,6,0,0],\
        [0,9,0,3,0,5,0,0,1],\
        [0,0,1,8,0,6,4,0,0],\
        [0,0,8,1,0,2,9,0,0],\
        [7,0,0,0,0,0,0,0,8],\
        [0,0,6,7,0,8,2,0,0],\
        [0,0,2,6,0,9,5,0,0],\
        [8,0,0,2,0,3,0,0,9],\
        [0,0,5,0,1,0,3,0,0]

        self.first_result = \
        [5,0,3,0,2,0,6,0,0],\
        [0,9,0,3,0,5,0,0,1],\
        [0,0,1,8,0,6,4,0,0],\
        [0,0,8,1,0,2,9,0,0],\
        [7,0,0,0,0,0,0,0,8],\
        [0,0,6,7,0,8,2,0,0],\
        [0,0,2,6,0,9,5,0,0],\
        [8,0,0,2,0,3,0,0,9],\
        [0,0,5,0,1,0,3,0,0]

        self.second_matrx= \
        [0,0,3,0,2,0,6,0,0],\
        [9,0,0,3,0,5,0,0,1],\
        [0,0,1,8,0,6,4,0,0],\
        [0,0,8,1,0,2,9,0,0],\
        [7,0,0,0,0,0,0,0,8],\
        [0,0,6,7,0,8,2,0,0],\
        [0,0,2,6,0,9,5,0,0],\
        [8,0,0,2,0,3,0,0,9],\
        [0,0,5,0,1,0,3,0,0]

        self.third_matrx= \
        [4,1,2,3,6,9,8,0,5], \
        [0,3,0,0,0,0,0,0,0], \
        [0,0,0,7,0,0,0,0,0], \
        [0,2,0,0,0,0,0,6,0], \
        [0,0,0,0,8,0,4,0,0], \
        [0,0,0,0,1,0,0,0,0], \
        [0,0,0,6,0,3,0,7,0], \
        [5,0,0,2,0,0,0,0,0], \
        [1,0,4,0,0,0,0,0,0]

        self.fourth_matrx= \
        [4,1,7,3,2,6,8,9,5], \
        [2,3,5,1,9,8,6,4,7], \
        [6,8,9,7,4,5,1,2,3], \
        [3,2,1,4,5,7,9,6,8], \
        [7,5,6,9,8,2,4,3,1], \
        [0,0,0,0,1,0,0,0,0], \
        [0,0,0,6,0,3,0,7,0], \
        [5,0,0,2,0,0,0,0,0], \
        [1,0,4,0,0,0,0,0,0]

        self.fifth_matrx= \
        [4,1,7,3,2,6,8,9,5], \
        [2,3,5,1,9,8,6,4,7], \
        [6,8,9,7,4,5,1,2,3], \
        [3,2,1,4,5,7,9,6,8], \
        [7,5,6,9,8,2,4,3,1], \
        [0,4,0,0,1,0,0,0,0], \
        [0,0,0,6,0,3,0,7,0], \
        [5,0,0,2,0,0,0,0,0], \
        [1,0,4,0,0,0,0,0,0]


        self.game = Game(self.first_matrx)
        self.algorithm = Backtracking(self.first_matrx, 9)
        self.block = Block()
        self.menu = MenuPlay(self.first_matrx)


    def test_validate_square(self):
        '''Verify that a position id validated

        '''
        value_entered = "A1:5"
        value_result = 5
        result = self.game.validate_square(value_entered)
        self.assertEqual(value_result, result)

    def test_validate_row(self):
        result = self.algorithm.validate_row(self.first_matrx, 5, 0, 0)
        self.assertEqual(True, result)

    def test_validate_column(self):
        result = self.algorithm.validate_column(self.first_matrx, 5, 0, 0)
        self.assertEqual(True, result)

    def test_validate_block(self):
        result = self.block.validate_block(self.first_matrx, 5, 0, 0)
        self.assertEqual(True, result)

    def test_validate_when_only_numbers_are_entered_by_user(self):
        '''Verify when only numbers are entered instead of a letter to refer a column

        '''
        value_entered = "5555"
        value_result = False
        result = self.game.validate_square(value_entered)
        self.assertEqual(False, result)

    def test_validate_when_only_letters_are_entered_by_user(self):
        '''Verify when only letters are entered instead of a number to refer a row

        '''
        value_entered = "dddd"
        value_result = False
        result = self.game.validate_square(value_entered)
        self.assertEqual(False, result)

    def test_validate_when_long_values_are_entered_by_user(self):
        '''Verify when long values are entered instead of only 4 values

        '''
        value_entered = "longvaluedddd"
        value_result = False
        result = self.game.validate_square(value_entered)
        self.assertEqual(False, result)

    def test_validate_when_spaces_are_entered_by_user(self):
        '''Verify when long values are entered instead of only 4 values

        '''
        value_entered = "   "
        value_result = False
        result = self.game.validate_square(value_entered)
        self.assertEqual(False, result)

    def test_validate_when_any_character_is_entered_by_user(self):
        '''Verify when any character is entered

        '''
        value_entered = "%&*("
        value_result = False
        result = self.game.validate_square(value_entered)
        self.assertEqual(False, result)

    def test_validate_when_a_character_is_entered_instead_of_number_for_square(self):
        '''Verify when a character $ is entered instead of number

        '''
        value_entered = "A0:$"
        value_result = False
        result = self.game.validate_square(value_entered)
        self.assertEqual(False, result)

    def test_validate_when_anything_was_entered_instead_of_colon(self):
        '''Verify when anything was entered instead of colon(:)

        '''
        value_entered = "A0$5"
        value_result = False
        result = self.game.validate_square(value_entered)
        self.assertEqual(False, result)

    def test_validate_the_position_when_hint_is_used(self):
        '''Verify the value entered when hint is used because a ? is used as value
        '''
        value_entered = "A1:?"
        value_result = False
        result = self.game.validate_square(value_entered)
        self.assertEqual(True, result)

    def test_validate_if_a_default_position_can_be_updated(self):
        '''Verify the value entered when hint is used because a ? is used as value
        '''
        value_entered = "C1:7"
        value_result = False
        result = self.game.validate_square(value_entered)
        self.assertEqual(False, result)


if __name__ == '__main__':
    unittest.main()

