import unittest
from coverage import coverage

cov = coverage()
cov.start()

#from readfiles_tests import TestReadFiles
#from norvig_tests import TestNorvigAlgorithm
#from solver_tests import TestSolver
#from convert_tests import TestConvert
from tests_sudoku import TestBacktracking
from tests_algorithm import TestAlgorithm
from tests_playing import TestPlaying

if __name__ == '__main__':
    suite = unittest.TestSuite()
    #suite.addTest(unittest.makeSuite(TestReadFiles))
    #suite.addTest(unittest.makeSuite(TestNorvigAlgorithm))
    #suite.addTest(unittest.makeSuite(TestSolver))
    #suite.addTest(unittest.makeSuite(TestConvert))
    suite.addTest(unittest.makeSuite(TestBacktracking))
    suite.addTest(unittest.makeSuite(TestAlgorithm))
    suite.addTest(unittest.makeSuite(TestPlaying))

    unittest.TextTestRunner(verbosity=4).run(suite)

    cov.stop()
    cov.save()

    cov.html_report()
