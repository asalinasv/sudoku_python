import unittest
from coverage import coverage


cov = coverage()
cov.start()

from tests_sudoku import TestBacktracking

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestBacktracking))
    unittest.TextTestRunner(verbosity=4).run(suite)

    cov.stop()
    cov.save()

    cov.html_report()

