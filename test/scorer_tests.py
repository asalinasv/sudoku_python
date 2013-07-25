import unittest
from Player.sudokuscorer import *

class TestSolver(unittest.TestCase):
    def setUp(self):

        
        self.matrix = [[0, 0, 3, 0, 2, 0, 6, 0, 0],
                    [9, 0, 0, 3, 0, 5, 0, 0, 1], \
                    [0, 0, 1, 8, 0, 6, 4, 0, 0], \
                    [0, 0, 8, 1, 0, 2, 9, 0, 0], \
                    [7, 0, 0, 0, 0, 0, 0, 0, 8], \
                    [0, 0, 6, 7, 0, 8, 2, 0, 0], \
                    [0, 0, 2, 6, 0, 9, 5, 0, 0], \
                    [8, 0, 0, 2, 0, 3, 0, 0, 9], \
                    [0, 0, 5, 0, 1, 0, 3, 0, 0]]

        self.sudscore = SudokuScorer(self.matrix)
        
### ******* Unittest for SudokuScorer class *************

    def test_if_scorer_returns_the_number_of_zeros_of_a_matrix(self):
        expected = 49
        self.assertEqual(expected,(-self.sudscore.start()+500)/10)

    def test_if_score_of_500_is_displayed_when_sudoku_is_completed(self):
        expected = 500
        self.assertEqual(expected,self.sudscore.scorer(0))

if __name__ == '__main__':
    unittest.main()
