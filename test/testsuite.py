import unittest
from coverage import coverage

cov = coverage()
cov.start()

from readfiles_tests import TestReadFiles
from norvig_tests import TestNorvigAlgorithm
from solver_tests import TestSolver
from convert_tests import TestConvert

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestReadFiles))
    suite.addTest(unittest.makeSuite(TestNorvigAlgorithm))
    suite.addTest(unittest.makeSuite(TestSolver))
    suite.addTest(unittest.makeSuite(TestConvert))
    
    unittest.TextTestRunner(verbosity=4).run(suite)

    cov.stop()
    cov.save()

    cov.html_report()
