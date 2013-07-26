import unittest
from coverage import coverage
cov = coverage(omit = ['test*.py'])
cov.start()

import os
import sys
sys.path.append('../src/Player')
sys.path.append('../src/solver')
sys.path.append('../src/Configuration')
sys.path.append('../src/Menu')

from tests_sudoku import TestBacktracking
from tests_algorithm import TestAlgorithm
from tests_playing import TestPlaying

from test_hints_displayer import TestHintsDisplayerClassAndMethods 
from test_generators import TestGeneratorClassAndMethods
from test_configuration_class import TestConfigurationClassAndMethods
from test_storer_class import TestStorerClassAndMethods
from test_storesetting_class import TestStorerSettingClassAndMethods
from test_readfile_class import TestFileReaderClassAndMethods

from convert_tests import TestConvert
from norvig_tests import TestNorvigAlgorithm
from readfiles_tests import TestReadFiles
from solver_tests import TestSolver
from scorer_tests import TestScorer
from savepartialgame_tests import TestGameSaver



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestBacktracking))
    suite.addTest(unittest.makeSuite(TestAlgorithm))
    suite.addTest(unittest.makeSuite(TestPlaying))
    
    suite.addTest(unittest.makeSuite(TestConfigurationClassAndMethods))
    suite.addTest(unittest.makeSuite(TestFileReaderClassAndMethods))
    suite.addTest(unittest.makeSuite(TestGeneratorClassAndMethods))
    suite.addTest(unittest.makeSuite(TestHintsDisplayerClassAndMethods))
    suite.addTest(unittest.makeSuite(TestStorerClassAndMethods))

    suite.addTest(unittest.makeSuite(TestConvert))
    suite.addTest(unittest.makeSuite(TestNorvigAlgorithm))
    suite.addTest(unittest.makeSuite(TestReadFiles))
    suite.addTest(unittest.makeSuite(TestSolver))
    suite.addTest(unittest.makeSuite(TestScorer))
    suite.addTest(unittest.makeSuite(TestGameSaver))


    


    unittest.TextTestRunner(verbosity=4).run(suite)

    cov.stop()
    cov.save()

    cov.html_report()
