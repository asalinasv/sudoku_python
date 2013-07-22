# Game classes, Main module that call all the classes to play Sudoku
# Author: Oscar Walker Tapia Merida - oscar.tapia@jalasoft.com
# Automation Class (Sudoku project) - 2013

import os
from solver import *
from commandline import *
from readconfiguration import *
from storer import *

class Welcome:
    
    def welcome(self):
        if not os.path.exists('EmptySudokus'):
            os.makedirs('EmptySudokus')
        if not os.path.exists('ResolvedSudokus'):
            os.makedirs('ResolvedSudokus')
        os.system('cls')
        print "******************Welcome to Sudoke game***********************\n"+\
                '\n'+"Please select an option to start:\n"
        print "1: Menu \n2: Exit"
        try:
            value = int(raw_input())
            if value == 1:
                return Menu().menu()
            if value == 2:
                return Exit().exit()
            else:
                print "Please insert a value from the list"
                return self.welcome()
        except ValueError:
            print "Please insert a value from the list"
            return self.welcome()

class Menu:
    
    def menu(self):
        os.system('cls')
        print '***Menu***\nPlease select an option:\n\
                1: Resolve sudoku from file\n\
                2: Resolve sudoku from command line\n\
                3: Generate sudoku\n\
                4: Configure Settings\n\
                5: Back to Welcome\n\
                6: Exit'
        try:
            value = int(raw_input())
            if value == 1:
                return FileResolver().resolvefromfile()
            if value == 2:
                return CmdResolver().resolvefromcmd()
            if value == 3:
                return SudokuGenerator().generatesudoku()
            if value == 4:
                return SettingsConfigurator().configuresettings()
            if value == 5:
                return Welcome().welcome()
            if value == 6:
                return Exit().exit()
            else:
                return self.menu()
        except ValueError:
            return self.menu()
            
class FileResolver():
    
    def resolvefromfile(self):
        os.system('cls')
        print "Please select a file to resolve a sudoku: \n"
        print "Available files to be resolved:"
        a = os.listdir('EmptySudokus')
        for i in a:
            print i
        print "\n\nOptions:\n1:Back to Menu\n2:Exit"
        print "\n\n\nHELP: Please copy the empty sudoku files in the "+\
                os.path.abspath("EmptySudokus")+" folder to be resolved"
        self.filer = raw_input('\n')
        if self.filer == '1':
            return Menu().menu()
        if self.filer == '2':
            return Exit().exit()
        else:
            if os.path.isfile('EmptySudokus\\'+self.filer):
                return SudokuDisplayer().display(self.filer)
            else:
                return self.resolvefromfile()

class SudokuDisplayer:
    def display(self,file):
        os.system('cls')
        solv = Solver(file)
        if solv.solvesudoku()== False:
            return FileResolver().resolvefromfile()
        else:
            print "\n\nOptions:\n1:Back to Menu\n2:Exit"
            self.filer = raw_input('\n')
            if self.filer == '1':
                return Menu().menu()
            if self.filer == '2':
                return Exit().exit()
            else:
                return 
                   
        
class CmdResolver:

    def resolvefromcmd(self):
        os.system('cls')
        cmd = CommandLine()
        cmd.solve_from_commandline()
        return

class SudokuGenerator:

    def generatesudoku(self):
        os.system('cls')
        print "\n\n ********** Under construction ****************"
        return

class SettingsConfigurator:

    def configuresettings(self):
        os.system('cls')
        print "*** Under COnstruction ***"
        return


class Exit:

    def exit(self):
        os.system('cls')
        print "Thanks for using Sudoku Game"
        return

if __name__ == "__main__":
    game = Welcome()
    game.welcome()
