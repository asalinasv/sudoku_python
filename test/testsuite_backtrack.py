import unittest
from coverage import coverage


cov = coverage()
cov.start()

from tests_sudoku import TestBacktracking
from tests_algorithm import TestAlgorithm
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestBacktracking))
    suite.addTest(unittest.makeSuite(TestAlgorithm))
    unittest.TextTestRunner(verbosity=4).run(suite)

    cov.stop()
    cov.save()

    cov.html_report()

