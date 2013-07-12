# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="Oscar Tapia"
__date__ ="$Jul 2, 2013 11:04:27 AM$"

import unittest
from solution import Read_and_Solve
import norvigm
import csv

class SudokuTest(unittest.TestCase):
    def setUp(self):

        self.readsolve = Read_and_Solve()
        self.txtfile = "juego.txt"
        self.csvfile = 'juegosu.csv'
        self.presolution = 'presolution.txt'

    def test_if_solver_is_able_to_read_a_txt_file(self):
        f1 = open(self.txtfile,'r')
        expected = f1.read()
        self.assertEqual(expected, self.readsolve.reading_txt(self.txtfile))

    def test_if_txt_has_a_matrix_of_9x9(self):
        expected = 81
        self.assertEqual(expected,self.readsolve.validate_size_txt(self.txtfile))

    def test_if_txt_has_values_from_0_to_9(self):
        expected = True  # ??????
        self.assertEqual(expected, self.readsolve.validate_values_txt(self.txtfile))

    def test_if_txt_sudoku_is_solved_correctly(self):
        f2 = open(self.presolution,'r')
        expected = f2.read()
        f2.close()
        self.assertEqual(expected, self.readsolve.solved_sudoku_txt(self.txtfile))

    def test_if_solver_is_able_to_read_a_csv_file(self):
        with open (self.csvfile,'rb') as csvfile:
            expected = list(csv.reader(csvfile))
        self.assertEqual(expected, self.readsolve.reading_csv(self.csvfile))

    def test_if_csv_has_a_matrix_of_9x9(self):
        expected = 81
        self.assertEqual(expected,self.readsolve.validate_size_csv(self.csvfile))

    def test_if_csv_has_values_from_0_to_9(self):
        expected = True
        self.assertEqual(expected,self.readsolve.validate_values_csv(self.csvfile))



### ******* Unittest for Nornig's Algorithm *************

    def test_if_sudoku_constructs_81_squares(self):
        expected = 81
        self.assertEqual(expected, norvigm.count_squares())

    def test_if_sudoku_constructs_27_sublines(self):
        expected = 27
        self.assertEqual(expected, norvigm.count_sublines())

    def test_if_square_has_3_units_in_the_submatrix(self):
        expected = 3
        self.assertEqual(expected, norvigm.count_units())

    def test_if_square_has_20_peers_in_the_submatrix(self):
        expected = 20
        self.assertEqual(expected, norvigm.count_peers())


    def test_if_novig_algorithm_is_receiving_data(self):
        pass

    def test_if_novig_algorithm_is_returning_solution(self):
        pass







if __name__ == '__main__':
    unittest.main()