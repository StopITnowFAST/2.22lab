# !/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
import students_tests

if __name__ == "__main__":
    testLoad = unittest.TestLoader()
    suites = testLoad.loadTestsFromModule(students_tests)

    testResult = unittest.TestResult()

    runner = unittest.TextTestRunner(verbosity=1)
    testResult = runner.run(suites)

    print("errors")
    print(len(testResult.errors))
    print("failures")
    print(len(testResult.failures))
    print("skipped")
    print(len(testResult.skipped))
    print("testsRun")
    print(testResult.testsRun)