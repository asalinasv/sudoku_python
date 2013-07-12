import unittest
from norvigalgorithm import *

class TestNorvigAlgorithm(unittest.TestCase):
    def setUp(self):
        self.stringtonorvig = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
        self.invalidstringtonorvig = '0030206009003050010018064000081029007000000080067082000026095008002030090050103001'
        self.hardpuzzle = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
        self.novalidpuzzle = '44....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
        self.norvig = NorvigAlgorithm()

### ******* Unittest for Nornig's Algorithm *************

    def test_if_squares_are_being_constructed_correctly(self):
        expected = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', \
                    'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', \
                    'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', \
                    'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', \
                    'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', \
                    'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', \
                    'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', \
                    'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', \
                    'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']
        self.assertEqual(expected,self.norvig.getsquares())

    def test_if_unitlist_is_being_constructed_correctly(self):
        f3 = open('unitlistexpected.txt','r')
        expected = f3.read()
        f3.close()
        self.assertEqual(expected,str(self.norvig.getunitlist()))

    def test_if_sudoku_constructs_81_squares(self):
        expected = 81
        self.assertEqual(expected, self.norvig.count_squares())

    def test_if_sudoku_constructs_27_sublines(self):
        expected = 27
        self.assertEqual(expected, self.norvig.count_sublines())

    def test_if_square_has_3_units_in_the_submatrix(self):
        expected = 3
        self.assertEqual(expected, self.norvig.count_units())

    def test_if_square_has_20_peers_in_the_submatrix(self):
        expected = 20
        self.assertEqual(expected, self.norvig.count_peers())

    def test_if_near_units_are_being_constructed_correctly_for_C2(self):
        unit = 'C2'
        expected = [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'], \
                    ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'], \
                    ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
        self.assertEqual(expected, self.norvig.near_units(unit))

    def test_if_near_peers_are_being_constructed_correctly_for_C2(self):
        peersof = 'C2'
        expected = set(['F2', 'G2', 'H2', 'D2', 'I2', 'C9', 'C6', 'A1', 'A3', 'C8', \
                        'B1', 'B2', 'B3', 'C3', 'C1', 'E2', 'C7', 'A2', 'C5', 'C4'])
        self.assertEqual(expected, self.norvig.near_peers(peersof))

    def test_if_easy_sudoku_is_solved_for_norvig_algorithm(self):
        expected = {'I6': '7', 'H9': '9', 'I2': '9', 'E8': '3', 'H3': '4', 'H7': '7',\
                    'I7': '3', 'I4': '4', 'H5': '5', 'F9': '5', 'G7': '5', 'G6': '9', \
                    'G5': '8', 'E1': '7', 'G3': '2', 'G2': '7', 'G1': '3', 'I1': '6', \
                    'C8': '9', 'I3': '5', 'E5': '6', 'I5': '1', 'C9': '3', 'G9': '4', \
                    'G8': '1', 'A1': '4', 'A3': '3', 'A2': '8', 'A5': '2', 'A4': '9', \
                    'A7': '6', 'A6': '1', 'C3': '1', 'C2': '5', 'C1': '2', 'E6': '4', \
                    'C7': '4', 'C6': '6', 'C5': '7', 'C4': '8', 'I9': '2', 'D8': '7', \
                    'I8': '8', 'E4': '5', 'D9': '6', 'H8': '6', 'F6': '8', 'A9': '7', \
                    'G4': '6', 'A8': '5', 'E7': '1', 'E3': '9', 'F1': '1', 'F2': '3', \
                    'F3': '6', 'F4': '7', 'F5': '9', 'E2': '2', 'F7': '2', 'F8': '4', \
                    'D2': '4', 'H1': '8', 'H6': '3', 'H2': '1', 'H4': '2', 'D3': '8', \
                    'B4': '3', 'B5': '4', 'B6': '5', 'B7': '8', 'E9': '8', 'B1': '9', \
                    'B2': '6', 'B3': '7', 'D6': '2', 'D7': '9', 'D4': '1', 'D5': '3', \
                    'B8': '2', 'B9': '1', 'D1': '5'}
        self.assertEqual(expected,self.norvig.solve(self.stringtonorvig))

    def test_if_hard_sudoku_is_solved_for_norvig_algorithm(self):
        expected = {'G7': '5', 'G6': '3', 'G5': '4', 'G4': '6', 'G3': '9', 'G2': '8', \
                    'G1': '2', 'G9': '1', 'G8': '7', 'C9': '6', 'C8': '1', 'C3': '8', \
                    'C2': '5', 'C1': '9', 'C7': '3', 'C6': '4', 'C5': '2', 'C4': '7', \
                    'E5': '8', 'E4': '5', 'F1': '3', 'F2': '4', 'F3': '6', 'F4': '9', \
                    'F5': '1', 'F6': '2', 'F7': '7', 'F8': '5', 'F9': '8', 'B4': '1', \
                    'B5': '5', 'B6': '8', 'B7': '9', 'B1': '6', 'B2': '3', 'B3': '2', \
                    'B8': '4', 'B9': '7', 'I9': '3', 'I8': '9', 'I1': '1', 'I3': '4', \
                    'I2': '6', 'I5': '7', 'I4': '8', 'I7': '2', 'I6': '5', 'A1': '4', \
                    'A3': '7', 'A2': '1', 'E9': '2', 'A4': '3', 'A7': '8', 'A6': '9', \
                    'A9': '5', 'A8': '2', 'E7': '4', 'E6': '6', 'E1': '7', 'E3': '1', \
                    'E2': '9', 'E8': '3', 'A5': '6', 'H8': '8', 'H9': '4', 'H2': '7', \
                    'H3': '3', 'H1': '5', 'H6': '1', 'H7': '6', 'H4': '2', 'H5': '9', \
                    'D8': '6', 'D9': '9', 'D6': '7', 'D7': '1', 'D4': '4', 'D5': '3', \
                    'D2': '2', 'D3': '5', 'D1': '8'}
        self.assertEqual(expected,self.norvig.solve(self.hardpuzzle))

    def test_if_sudoku_can_handle_invalid_inputs(self):
        expected = False
        self.assertEqual(expected,self.norvig.solve(self.invalidstringtonorvig))

    def test_if_grid_values_method_is_handling_invalid_inputs(self):
        expected = False
        self.assertEqual(expected,self.norvig.grid_values(self.invalidstringtonorvig))

    def test_if_display_method_is_handling_invalid_values(self):
        result = self.norvig.grid_values(self.invalidstringtonorvig)
        expected = False
        self.assertEqual(expected,self.norvig.display(result))

    def test_if_display_method_can_print_the_result(self):
        result = self.norvig.grid_values(self.stringtonorvig)
        expected = True
        self.assertEqual(expected,self.norvig.display(result))

    def test_if_near_squares_are_validated(self):
        expected = False
        self.assertEqual(expected,self.norvig.parse_grid(self.novalidpuzzle))

if __name__ == '__main__':
    unittest.main()
