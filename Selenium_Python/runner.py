import unittest
from unittest.suite import TestSuite
import register, login, shoppingcart_checkout

if __name__ == "__main__":
    # create test suite from classes
    suite = TestSuite()

    # call test
    tests = unittest.TestLoader()

    # add test to suite
    suite.addTest(tests.loadTestsFromModule(register))
    suite.addTest(tests.loadTestsFromModule(login))
    suite.addTest(tests.loadTestsFromModule(shoppingcart_checkout))

    # run the test suite
    runner = unittest.TextTestRunner()
    runner.run(suite)