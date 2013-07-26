from sudokuscorer import *
import os
from time import gmtime, strftime
import time
import sys
sys.path.append('../')

class GameSaver:
    def __init__(self,matrix):
        self.matrix = matrix

    def savegame(self):
        """Saves the game in the SavedSudokus folder"""
        gamesaved = self.matrix
        score = SudokuScorer(self.matrix).start()
        try:
            import cPickle as pickle
        except ImportError:
            import pickle
        if not os.path.exists('../Player/SavedSudokus'):
            os.makedirs('../Player/SavedSudokus')
        fichero = file("../Player/SavedSudokus\\"+strftime("%Y%m%d%H%M%S", gmtime())+".dat", "w")
        objetos = [gamesaved,score]
        pickle.dump(objetos, fichero)
        fichero.close()
        os.system('cls')
        print "\nThe game was sucessfully saved"
        time.sleep(3.0)
        return True

    def loadgame(self):
        """Loads a game from SavedSudokus folder"""
        if not os.path.exists('../Player/SavedSudokus'):
            os.makedirs('../Player/SavedSudokus')
        a = os.listdir('../Player/SavedSudokus')
        print "Saved games: "
        for i in a:
            print i
        loadfile = raw_input('Please specify the game to be loaded:\n ')
        if os.path.isfile('../Player/SavedSudokus\\'+loadfile):
            loadfile = os.path.abspath('../Player/SavedSudokus\\'+loadfile)
            try:
                import cPickle as pickle
            except ImportError:
                import pickle
            fichero = file(loadfile)
            objeto = pickle.load(fichero)
            return objeto[0]
        else:
            print "Please try again with a saved game"
            self.loadgame()