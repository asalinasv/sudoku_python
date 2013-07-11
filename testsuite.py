import unittest
from coverage import coverage
cov = coverage()
cov.start()

from sudoUT import TestReadFiles

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestReadFiles))
    
    
    

    unittest.TextTestRunner(verbosity=4).run(suite)

    cov.stop()
    cov.save()

    cov.html_report()
