from Player.sudokusavepartialgame import *
import unittest
from solver.norvigalgorithm import *

class TestGameSaver(unittest.TestCase):
    def setUp(self):
        self.matrix= \
        [1,1,3,1,2,0,6,0,0],\
        [0,9,0,3,0,5,0,0,1],\
        [0,0,1,8,0,6,4,0,0],\
        [0,0,8,1,0,2,9,0,0],\
        [7,0,0,0,0,0,0,0,8],\
        [0,0,6,7,0,8,2,0,0],\
        [0,0,2,6,0,9,5,0,0],\
        [8,0,0,2,0,3,0,0,9],\
        [0,0,5,0,1,0,3,0,0]

        self.gamesaver = GameSaver(self.matrix)

### ******* Unittest for GameSaver class *************

    def test_if_game_is_partial_saved(self):
        expected = True
        self.assertEqual(expected,self.gamesaver.savegame())

if __name__ == '__main__':
    unittest.main()