import unittest
from sudokubacktrack import Algorithm

class TestAlgorithm(unittest.TestCase):

      def setUp(self):
          self.new_dimension = 9
          self.algorithm = Algorithm(self.new_dimension)

      def test_algorithm_should_verify_correct_dimension(self):
          '''verify if the dimension is received correctly'''
          result = self.algorithm.get_matrix()
          self.assertEqual(9, result)

if __name__ == '__main__':
    unittest.main()
