#-------------------------------------------------------------------------------
# Name:        playing_sudoku
# Purpose:     validate squares entered by the gamer
# Author:      Israel Azurduy
# Email:       israel.azurduy@gmail.com
# Created:     19/07/2013
# Copyright:   (c) Israel Azurduy 2013
#-------------------------------------------------------------------------------
import os
from sys import path
path.append("../src/solver/")
from sudokubacktrack import Backtracking
from sudokubacktrack import Block
#from display import SudokuDisplayer

class Game():
      def __init__(self, matrix): #, row, col):
          self.matrix = matrix
          self.letters = {'A': 0,'a': 0,'B': 1,'b': 1,'C': 2,'c': 2,'D': 3,'d': 3,'E': 4,'e': 4, \
                       'F': 5,'f': 5,'G': 6,'g': 6,'H': 7,'h': 7,'I': 8,'i': 8}
          self.row = 0 #row
          self.col = 0 #column
          self.value = 0
          self.val_row_col = Backtracking(self.matrix,9)
          self.val_block = Block()


      def fill_square(self, value):
          '''Fill each square

          '''

          self.matrix [self.row][self.col] = value
          return 0

      def validate_square(self, square):
          if len(square) == 4:

              try:
                  self.row = int(square[1])
              except:
                     return False

              try:
                  self.col = (self.letters[square[0]]) #self.col = int(square[0])
              except:
                     return False
              try:
                  self.value = int(square[3])
              except:
                     return False

              if (square[2] != ":"):
                 return False

              if self.value <= 9:
                 '''Verify when the value is less than 10

                 '''
                 if self.val_row_col.validate_column(self.matrix, self.value, self.row, self.col) and \
                      self.val_row_col.validate_row(self.matrix, self.value, self.row, self.col) and \
                      self.val_block.validate_block(self.matrix, self.value, self.row, self.col):
                      return self.value
                 else:
                      return False #"You need a HINT... because the value exists"

              else:
                   return False # when the value is incorrect retunr False

          else:
               return False # when the value is incorrect retunr False


      def validate_value(self, value):
          if value > 9:
             return False
          #if



      def display_game(self):
          os.system('cls')
          print "***************Welcome to interactive Sudoku game***************\n"
          row = 0
          col = 0
          while row < 9:
                while col < 9:
                      print self.matrix[row][col],
                      col += 1
                col = 0
                print '\n'
                row += 1

          return 0

class Menu:
      def __init__(self, matrix):
          self.matrix = matrix
          self.game = Game(self.matrix)
          #self.game = SudokuDisplayer(self.matrix)
      def menu(self):
          value = 0
          os.system('cls')
##          self.game.display_game(self)
          ##Game(self.matrix).display_game()
          self.game.display_game()
          #self.game.display()
          option = raw_input("\t  - Enter 'M' if you want to return to Menu\n\
          - Enter 'S' if you want to Save the game\n\
          - Enter 'H' if you want to play with HINTS\n\
          - Enter 'E' if you want to Exit the game\n\
          - Enter the position followed by colon and the value of square (e.g. C7:9): ")

          if option == "M" or option == "m":
             print "Go to Menu --- need to be completed"
          elif option == "S" or option == "s":
               print "Go to SAVE game --- need to be completed"
          else:
               if option == "H" or option == "h":
                  print "Go to HINTS --- need to be completed"
               elif option == "E" or option == "e":
                    Exit().exit()
               else:
                    value = self.game.validate_square(option)
                    if value != False:
                       self.game.fill_square(value)
                    self.menu()


          return

class Exit:
    def exit(self):
        os.system('cls')
        print "Thanks for using Sudoku Game"
        return


##def main():
##    pass
##
if __name__ == '__main__':
    matrix= \
    [0,0,3,0,2,0,6,0,0],\
    [0,9,0,3,0,5,0,0,1],\
    [0,0,1,8,0,6,4,0,0],\
    [0,0,8,1,0,2,9,0,0],\
    [7,0,0,0,0,0,0,0,8],\
    [0,0,6,7,0,8,2,0,0],\
    [0,0,2,6,0,9,5,0,0],\
    [8,0,0,2,0,3,0,0,9],\
    [0,0,5,0,1,0,3,0,0]
    jugar = Menu(matrix)
    jugar.menu()
    #retorno = jugar.fill_square()
##    while jugar.fill_square() != "exit":
##          jugar.validate_square()
##    print jugar.validate_square()

