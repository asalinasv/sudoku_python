import unittest
from coverage import coverage

cov = coverage()
cov.start()

from readfiles_tests import TestReadFiles
from norvig_tests import TestNorvigAlgorithm
from solver_tests import TestSolver
from convert_tests import TestConvert
from tests_sudoku import TestBacktracking
from test_configuration_class import TestConfigurationClassAndMethods
#from test_readfile_class import TestFileReaderClassAndMethods
#from test_sort import TestSortLists
from test_storer_class import TestStorerClassAndMethods
from test_storesetting_class import TestStorerSettingClassAndMethods


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestReadFiles))
    suite.addTest(unittest.makeSuite(TestNorvigAlgorithm))
    suite.addTest(unittest.makeSuite(TestSolver))
    suite.addTest(unittest.makeSuite(TestConvert))
    suite.addTest(unittest.makeSuite(TestBacktracking))
    suite.addTest(unittest.makeSuite(TestConfigurationClassAndMethods))
  #  suite.addTest(unittest.makeSuite(TestFileReaderClassAndMethods))
 #   suite.addTest(unittest.makeSuite(TestSortLists))
    suite.addTest(unittest.makeSuite(TestStorerClassAndMethods))
    suite.addTest(unittest.makeSuite(TestStorerSettingClassAndMethods))


    unittest.TextTestRunner(verbosity=4).run(suite)

    cov.stop()
    cov.save()

    cov.html_report()
