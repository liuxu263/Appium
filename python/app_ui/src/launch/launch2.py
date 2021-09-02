#! /user/bin/env python
# -*- coding:utf-8 -*-

import unittest

from python.app_ui.src.testsuites.testsuite2 import TestSuite2

if __name__ == '__main__':
    suite = TestSuite2().suite
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
