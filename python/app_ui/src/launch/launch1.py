#! /user/bin/env python
# -*- coding:utf-8 -*-

import unittest

from python.app_ui.src.testsuites.testsuite1 import TestSuite1

if __name__ == '__main__':
    suite = TestSuite1().suite
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
