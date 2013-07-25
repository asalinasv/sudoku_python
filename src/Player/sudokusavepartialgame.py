from sudokuscorer import *
import os
from time import gmtime, strftime

class GameSaver:
    def __init__(self,matrix):
        self.matrix = matrix

    def savegame(self):
        gamesaved = self.matrix
        score = SudokuScorer(self.matrix).start()
        try:
            import cPickle as pickle
        except ImportError:
            import pickle
        if not os.path.exists('SavedSudokus'):
            os.makedirs('../Player/SavedSudokus')
        fichero = file("../Player/SavedSudokus\\"+strftime("%Y%m%d%H%M%S", gmtime())+".dat", "w")
        objetos = [gamesaved,score]
        pickle.dump(objetos, fichero)
        fichero.close()
        return True

    def loadgame(self):
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
            print objeto[0]
            return objeto[0]
        else:
            print "porque no carga"
            self.loadgame()
        

ash= \
        [1,1,3,1,2,0,6,0,0],\
        [0,9,0,3,0,5,0,0,1],\
        [0,0,1,8,0,6,4,0,0],\
        [0,0,8,1,0,2,9,0,0],\
        [7,0,0,0,0,0,0,0,8],\
        [0,0,6,7,0,8,2,0,0],\
        [0,0,2,6,0,9,5,0,0],\
        [8,0,0,2,0,3,0,0,9],\
        [0,0,5,0,1,0,3,0,0]

#game = GameSaver(ash)
#game.savegame()
#game.loadgame()
