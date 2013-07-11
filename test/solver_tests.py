import unittest
from solver import Solver

class TestSolver(unittest.TestCase):
    def setUp(self):
        self.solver_txt = Solver("juego.txt")
        self.solver_csv = Solver("juego.csv")
        self.solver_invalidtxt = Solver("juego1.txt")
        self.solver_invalidcsv = Solver("juego1.csv")
        self.solver_other = Solver("juego.png")
        self.resultpuzzle = '483921657967345821251876493548132976729564138136798245372689514814253769695417382'
        
### ******* Unittest for solver class *************

    def test_if_solver_resolves_a_sudoku_from_a_TXT_file_using_norvig_algorithm(self):
        expected = self.resultpuzzle
        self.assertEqual(expected,self.solver_txt.norvig_algorithm())
        
    def test_if_solver_handle_invalid_TXT_file_using_norvig_algorithm(self):
        expected = "Please insert the correct data and size in the txt file"
        self.assertEqual(expected,self.solver_invalidtxt.norvig_algorithm())

    def test_if_solver_resolves_a_sudoku_from_a_CSV_file_using_norvig_algorithm(self):
        expected = self.resultpuzzle
        self.assertEqual(expected,self.solver_csv.norvig_algorithm())

    def test_if_solver_handle_invalid_CSV_file_using_norvig_algorithm(self):
        expected = "Please insert the correct data and size in the csv file"
        self.assertEqual(expected,self.solver_invalidcsv.norvig_algorithm())

    def test_if_solver_returns_a_friendly_message_when_invalid_file_is_inserted(self):
        expected = 'invalid extension'
        self.assertEqual(expected,self.solver_other.norvig_algorithm())

    def test_if_solution_is_stored_in_a_txt_file(self):
        f1 = open("presolution.txt",'r')
        expected = f1.read()
        f1.close()
        self.assertEqual(expected,self.solver_txt.store_solution_in_txt_file())

if __name__ == '__main__':
    unittest.main()
