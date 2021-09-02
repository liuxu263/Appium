#! /user/bin/env python
# -*- coding:utf-8 -*-

import unittest

from python.app_ui.src.testcases.testcase1 import Test1
from python.app_ui.src.testcases.testcase2 import Test2


class TestSuite2(object):
    suite = unittest.TestSuite()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Test1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(Test2)

    suite.addTest(suite1)
    suite.addTest(suite2)
