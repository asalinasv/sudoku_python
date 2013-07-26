#-------------------------------------------------------------------------------
# Name:        playing_sudoku
# Purpose:     validate squares entered by the gamer
# Author:      Israel Azurduy
# Email:       israel.azurduy@gmail.com
# Created:     19/07/2013
# Copyright:   (c) Israel Azurduy 2013
#-------------------------------------------------------------------------------
import os
import sys
import copy
sys.path.append('../')
#from sys import path
##path.append("../src/solver/")
sys.path.append('../../src')
from solver.sudokubacktrack import *
from solver.storer import *
from solver.display import *
from Player.sudokusavepartialgame import *
#from Menu.game import *
#from solver.sudokubacktrack import Block
from Player.hint_displayer import *

class Game():
      def __init__(self, matrix): #, row, col):
          self.matrix_orig = copy.deepcopy(matrix)
          self.matrix_one = matrix

          self.letters = {'A': 0,'a': 0,'B': 1,'b': 1,'C': 2,'c': 2,'D': 3,'d': 3,'E': 4,'e': 4, \
                       'F': 5,'f': 5,'G': 6,'g': 6,'H': 7,'h': 7,'I': 8,'i': 8}
          self.row = 0 #row
          self.col = 0 #column
          self.value = 0
          self.val_row_col = Backtracking(self.matrix_one,9)
          self.val_block = Block()


      def fill_square(self, value):
          '''Fill each square

          '''

          self.matrix_one [self.row][self.col] = value
          return 0

      def validate_square(self, square):
          if len(square) == 4:

              try:
                  self.row = int(square[1])-1 # verify the row
              except:
                     return False

              try:
                  self.col = (self.letters[square[0]]) #validate the column
              except:
                     return False
              try:
                  self.value = int(square[3]) # validate the value
              except:
                     if square[3] == "?":
                        return True
                     else:
                          return False

              if (square[2] != ":"): # validate the colon
                 return False

              if self.matrix_orig[self.row][self.col] != 0: # validate default value
                 return False

              if self.value <= 9:
                 '''Verify when the value is less than 10

                 '''
                 if self.val_row_col.validate_column(self.matrix_one, self.value, self.row, self.col) and \
                      self.val_row_col.validate_row(self.matrix_one, self.value, self.row, self.col) and \
                      self.val_block.validate_block(self.matrix_one, self.value, self.row, self.col):
                      return self.value
                 else:
                      return False #"You need a HINT... because the value exists"

              else:
                   return False # when the value is incorrect retunr False

          else:
               return False # when the size is greather than 4


      def display_game(self):
          os.system('cls')
          print "***************Welcome to interactive Sudoku game***************\n"
          row = 0
          col = 0
          row_value = 0
          print "\tA-B-C-D-E-F-G-H-I"
          while row < 9:
                row_value = row + 1
                print str(row_value) + "|", '\t',

                while col < 9:
                      print self.matrix_one[row][col],
                      col += 1
                col = 0
                print '\n'
                row += 1

          return 0

class MenuPlay:
      def __init__(self, matrix):
          matrix = tuple(matrix)
          self.matrix_one = matrix
          print "the TYPE ISSSSSSSS in menu play"
          print type(self.matrix_one)
          print self.matrix_one
          self.game = Game(self.matrix_one)
          self.hint = HintsDisplayer(self.matrix_one)
          self.save = GameSaver(self.matrix_one)#Storer(self.matrix_one, "game_customer1", "txt")
          #self.game = SudokuDisplayer(self.matrix)
      def menu(self):
          self.game = Game(self.matrix_one)
          value = 0
          value_sug = 0
          position = ""
          os.system('cls')
##          self.game.display_game(self)
          ##Game(self.matrix).display_game()
          #self.game.display_game() other display
          SudokuDisplayer(self.matrix_one).displaysudoku()
          SudokuScorer(self.matrix_one).start()
          #self.game.display()
          option = raw_input("\
          - Enter 'M' if you want to return to MenuPlay\n\
          - Enter 'L' if you want to Open a saved game\n\
          - Enter 'H' if you want to play with HINTS\n\
          - Enter 'S' if you want to Save the game\n\
          - Enter 'E' if you want to Exit the game\n\
          - Enter the position followed by colon and the value of square (e.g. C7:9): ")

          if option == "M" or option == "m":
             print "Go to Menu --- need to be completed"
             return

          if option == "L" or option == "l":
             self.matrix_one = self.open_saved_game()
             #MenuPlay(self.matrix_one)
             print "Go to OPEN a saved game --- need to be completed"
             #self.menu()

          if option == "H" or option == "h":
             position = raw_input("Insert the column and row to receive the Hint (e.g. A1): ")
             position = position + ":?"
##             print "the psition is %s" %position
##             retonr = self.game.validate_square(position)
##             print retonr
             if self.game.validate_square(position):
                '''To verify that position entered is correct

                '''
                value_sug = self.hint.get_value_in_cell(position[0] + position[1])
                self.game.fill_square(value_sug)
             else:
                  print "the value is INCORRECT"
                  print self.hint.get_value_in_cell("A1")

             print "Go to HINTS --- need to be completed"

          if option == "S" or option == "s":
             self.save_option()
             print "Go to SAVE game --- need to be completed"

          if option == "E" or option == "e":
             Exit().exit()
          else:
            value = self.game.validate_square(option)
            if value != False:
               self.game.fill_square(value)
            self.menu()
          return

      def save_option(self):
          self.save.matrix = self.matrix_one
          self.save.savegame()
          return

      def open_saved_game(self):
          matrix_saved = self.save.loadgame()
          print "SALIO deLCICLO"
          print matrix_saved
          self.matrix_one = matrix_saved

          return  matrix_saved


class Exit:
    def exit(self):
        os.system('cls')
        print "Thanks for using Sudoku Game"
        return


##if __name__ == '__main__':
##    matrix= \
##    [0,0,3,0,2,0,6,0,0],\
##    [0,9,0,3,0,5,0,0,1],\
##    [0,0,1,8,0,6,4,0,0],\
##    [0,0,8,1,0,2,9,0,0],\
##    [7,0,0,0,0,0,0,0,8],\
##    [0,0,6,7,0,8,2,0,0],\
##    [0,0,2,6,0,9,5,0,0],\
##    [8,0,0,2,0,3,0,0,9],\
##    [0,0,5,0,1,0,3,0,0]
##    jugar = MenuPlay(matrix)
##    jugar.menu()



