import unittest
from solver.solver import *

class TestSolver(unittest.TestCase):
    def setUp(self):

        self.txtfile = os.path.abspath("../src/Menu/EmptySudokus/juego.txt")
        self.txtfile1 = os.path.abspath("../src/Menu/EmptySudokus/juego1.txt")
        self.csvfile = os.path.abspath("../src/Menu/EmptySudokus/juego.csv")
        self.csvfile1 = os.path.abspath("../src/Menu/EmptySudokus/juego1.csv")
        self.solver_txt = Solver(self.txtfile)
        self.solver_csv = Solver(self.csvfile)
        self.solver_invalidtxt = Solver(self.txtfile1)
        self.solver_invalidcsv = Solver(self.csvfile1)
        self.solver_other = Solver("juego.png")
        self.resultpuzzle =  [['4', '8', '3', '9', '2', '1', '6', '5', '7'], \
                                ['9', '6', '7', '3', '4', '5', '8', '2', '1'], \
                                ['2', '5', '1', '8', '7', '6', '4', '9', '3'], \
                                ['5', '4', '8', '1', '3', '2', '9', '7', '6'], \
                                ['7', '2', '9', '5', '6', '4', '1', '3', '8'], \
                                ['1', '3', '6', '7', '9', '8', '2', '4', '5'], \
                                ['3', '7', '2', '6', '8', '9', '5', '1', '4'], \
                                ['8', '1', '4', '2', '5', '3', '7', '6', '9'], \
                                ['6', '9', '5', '4', '1', '7', '3', '8', '2']]

        self.solverconfig1 = Solver(self.txtfile)
        absolutepath = os.path.abspath("../test/config1.ini")
        self.solverconfig1.readconf = FileReader(absolutepath)
        self.solverconfig2 = Solver(self.txtfile)
        absolutepath = os.path.abspath("../test/config2.ini")
        self.solverconfig2.readconf = FileReader(absolutepath)
        #self.readconf = FileReader(absolutepath)
        
### ******* Unittest for solver class *************

    def test_if_solver_resolves_a_sudoku_from_a_TXT_file_using_norvig_algorithm(self):
        expected = self.resultpuzzle
        self.assertEqual(expected,self.solver_txt.solve_using_norvig_algorithm())
        
    def test_if_solver_handle_invalid_TXT_file_using_norvig_algorithm(self):
        expected = False
        self.assertEqual(expected,self.solver_invalidtxt.solve_using_norvig_algorithm())

    def test_if_solver_resolves_a_sudoku_from_a_CSV_file_using_norvig_algorithm(self):
        expected = self.resultpuzzle
        self.assertEqual(expected,self.solver_csv.solve_using_norvig_algorithm())

    def test_if_solver_handle_invalid_CSV_file_using_norvig_algorithm(self):
        expected = "Please insert the correct data and size in the csv file"
        self.assertEqual(expected,self.solver_invalidcsv.solve_using_norvig_algorithm())

    def test_if_solver_returns_a_friendly_message_when_invalid_file_is_inserted(self):
        expected = 'invalid extension'
        self.assertEqual(expected,self.solver_other.solve_using_norvig_algorithm())

    def test_if_solver_resolves_a_sudoku_from_a_TXT_file_using_backtracking_algorithm(self):
        expected = self.resultpuzzle
        self.assertEqual(expected,self.solver_txt.solve_using_backtracking_algorithm())

    def test_if_solver_handle_invalid_TXT_file_using_backtracking_algorithm(self):
        expected = 'Please insert the correct data and size in the txt file'
        self.assertEqual(expected,self.solver_invalidtxt.solve_using_backtracking_algorithm())

    def test_if_solver_resolves_a_sudoku_from_a_CSV_file_using_backtracking_algorithm(self):
        expected = self.resultpuzzle
        self.assertEqual(expected,self.solver_csv.solve_using_backtracking_algorithm())

    def test_if_solver_handle_invalid_CSV_file_using_backtracking_algorithm(self):
        expected = "Please insert the correct data and size in the csv file"
        self.assertEqual(expected,self.solver_invalidcsv.solve_using_backtracking_algorithm())

    def test_if_solver_returns_a_friendly_message_when_invalid_file_is_inserted_backtracking(self):
        expected = 'invalid extension'
        self.assertEqual(expected,self.solver_other.solve_using_backtracking_algorithm())

    def test_if_main_solver_method_sends_a_friendly_message_for_invalid_values_in_config_file(self):
        expected = False
        self.assertEqual(expected, self.solver_txt.solvesudoku())

    def test_if_main_solver_method_sends_to_norvig_algorithm_when_is_specified_in_config_file(self):
        expected = self.solverconfig1.solve_using_norvig_algorithm()
        self.assertEqual(expected, self.solverconfig1.solvesudoku())

    def test_if_main_solver_method_sends_to_backtracking_algorithm_when_is_specified_in_config_file(self):
        expected = self.solverconfig2.solve_using_backtracking_algorithm()
        self.assertEqual(expected, self.solverconfig2.solvesudoku())

if __name__ == '__main__':
    unittest.main()
