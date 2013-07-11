import unittest
import copy
from sudokubacktrack import Backtracking
from sudokubacktrack import Block

class TestBacktracking(unittest.TestCase):

    def setUp(self):

        # self.default_matrx= \
        # [4,1,7,3,2,6,8,9,5], \
        # [2,3,5,1,9,8,6,4,7], \
        # [6,8,9,7,5,4,3,1,2], \
        # [7,2,8,9,4,5,1,6,3], \
        # [0,0,0,0,8,0,4,0,0], \
        # [0,0,0,0,1,0,0,0,0], \
        # [0,0,0,6,0,3,0,7,0], \
        # [5,0,0,2,0,0,0,0,0], \
        # [1,0,4,0,0,0,0,0,0]

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

        #self.matrix = Backtracking()
        #self.matrix_copy=copy.deepcopy(self.default_matrx)
        self.matrix_copy=self.default_matrx
        self.matrix = Backtracking(self.default_matrx,9)
        self.block = Block()
        #[4,0,3,9,2,1,6,0,0]
        #[0,9,7,3,4,5,0,0,1]

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


        self.matrix_first = Backtracking(self.first_matrx,9)
        self.matrix_no = Backtracking(self.third_matrx,9)
        self.matrix_yes = Backtracking(self.second_matrx,9)
        # self.matrix_sixth = Backtracking(self.sixth_matrx,9)
        #self.matrix = Backtracking(self.second_matrx,9)
        #self.matrix = Backtracking(self.fifth_matrx,9)
        #self.matrix = Backtracking(self.fourth_matrx,9)
        #self.matrix = Backtracking(self.third_matrx,9)

    # def test_backtracking_should_do_nothing_if_board_is_filled(self):
    #     result = self.block.validate_block(self.default_matrx,4,3,2)
    #     self.assertEqual(False, result)

    def test_backtracking_should_back_when_the_value_number_is_wrong(self):
        pass

    def test_backtracking_should_create_the_board_with_new_values(self):
        pass


    # def test_backtracking_should_verify_if_value_does_exist_on_row(self):
    #     result=sudoku_backtracking.validate_row(self.default_matrx,2,0,1)
    #     self.assertEqual(True, result)

    # def test_backtracking_should_verify_if_value_exist_on_column(self):
    #     result=sudoku_backtracking.validate_column(self.default_matrx,1,7,7)
    #     self.assertEqual(True, result)

    def test_block_validate_should_verify_that_value_does_not_exist_on_block_one(self):
        result = self.block.validate_block(self.default_matrx,1,0,0)
        self.assertEqual(True, result)

    def test_block_validate_should_verify_that_value_does_not_exist_on_block_two(self):
        result = self.block.validate_block(self.default_matrx,2,2,3)
        self.assertEqual(True, result)

    def test_block_validate_should_verify_that_value_does_not_exist_on_block_three(self):
        result = self.block.validate_block(self.default_matrx,9,1,8)
        self.assertEqual(True, result)

    def test_block_validate_block_should_verify_that_value_does_not_exist_on_block_four_test(self):
        '''Sending value, row and column to know if the value exist on the block '''
        result = self.block.validate_block(self.default_matrx,4,3,2)
        self.assertEqual(True, result)

    def test_block_validate_block_should_verify_that_value_does_not_exist_on_block_five(self):
        result = self.block.validate_block(self.default_matrx,9,5,4)
        self.assertEqual(True, result)

    def test_block_validate_block_should_verify_that_value_does_not_exist_on_block_six(self):
        result = self.block.validate_block(self.default_matrx,3,5,7)
        self.assertEqual(True, result)

    def test_block_validate_block_should_verify_that_value_does_not_exist_on_block_seven(self):
        result = self.block.validate_block(self.default_matrx,8,7,1)
        self.assertEqual(True, result)

    def test_block_validate_block_should_verify_that_value_does_not_exist_on_block_eight(self):
        result = self.block.validate_block(self.default_matrx,5,7,5)
        self.assertEqual(True, result)

    def test_block_validate_block_should_verify_that_value_does_not_exist_on_block_nine(self):
        result = self.block.validate_block(self.default_matrx,6,8,8)
        self.assertEqual(True, result)

    def test_backtracking_should_validate_that_value_can_be_used_on_square(self):
        pass

    def test_block_define_position_of_block_in_row_should_be_returned(self):
        result = self.block.define_position_of_block(4)
        self.assertEqual(3, result)

    def test_block_define_position_of_block_in_column_should_be_returned(self):
        result = self.block.define_position_of_block(7)
        self.assertEqual(6, result)

    def test_block_get_initial_positions_for_block_should_verify_if_the_correct_initial_values_for_row_three_and_column_two_are_returned(self):
        'Sending row and column'
        result = self.block.get_initial_positions_for_block(3,2)
        self.assertEqual((3,0), result)

    def test_block_get_initial_positions_for_block_should_verify_if_the_correct_initial_values_for_row_zero_and_column_six_are_returned(self):
        result = self.block.get_initial_positions_for_block(0,6)
        self.assertEqual((0,6), result)



    def test_back_previous_solution_should_return_value_row_and_column(self):
        result = self.matrix.back_previous_solution(self.third_matrx,0,7)
        self.assertEqual((7,0,4),result)


    # def test_solve_backtracking_should_verify_that_is_unable_to_solve_fourth_matrix_with_five_files_filled(self):
    #     result = self.matrix.solve_backtracking(self.fourth_matrx)
    #     print "The fourth matrix is: \n"
    #     print self.fourth_matrx
    #     print "The result is: \n"
    #     print result
    #     self.assertEqual(self.fourth_matrx,result)

    # def test_solve_backtracking_should_verify_when_column_is_zero_and_value_nine(self):
    #     self.matrix = Backtracking(self.fifth_matrx,9)
    #     result = se lf.matrix.solve_backtracking(self.fifth_matrx)
    #     print "The fifth matrix is: \n"
    #     print self.fifth_matrx
    #     print "The result is: \n"
    #     print result
    #     self.assertEqual(self.fifth_matrx,result)

    # def test_solve_backtracking_should_verify_that_is_unable_to_solve_the_first_matrix(self):
    #     result = self.matrix.solve_backtracking(self.default_matrx)
    #     print "The default matrix is: \n"
    #     print self.default_matrx
    #     print "The result is: \n"
    #     print result
    #     self.assertEqual(self.matrix_copy,result)

    def test_solve_backtracking_should_verify_that_is_able_to_solve_the_first_matrix(self):
        '''Verify if is able to retuirna row when a default 9 value is in row 1 and column 1'''
        result = self.matrix_first.solve_backtracking(self.first_matrx)
        print "The First matrix is: \n"
        print self.first_matrx
        print "The result is: \n"
        print result
        self.assertEqual(self.first_matrx,result)

    def test_solve_backtracking_should_verify_that_is_able_to_solve_the_second_matrix(self):
        result = self.matrix_yes.solve_backtracking(self.second_matrx)
        print "The second matrix is: \n"
        print self.second_matrx
        print "The result is: \n"
        print result
        self.assertEqual(self.second_matrx,result)


    def test_solve_backtracking_should_verify_that_is_unable_to_solve_the_third_matrix(self):
        result = self.matrix_no.solve_backtracking(self.third_matrx)
        print "The third_matrx matrix is: \n"
        print self.third_matrx
        print "The result is: \n"
        print result
        self.assertEqual(self.third_matrx,result)

if __name__ == '__main__':
    unittest.main()
