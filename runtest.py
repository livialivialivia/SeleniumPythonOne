#! /usr/bin/env python
# _*_ coding: utf-8 _*_

import unittest
from test_case import BaiDu_Search
from test_case import BaiDu_Set

suite = unittest.TestSuite()
suite.addTest(BaiDu_Search.BaiDuSearch('test_baidu_search'))
suite.addTest(BaiDu_Set.BaiDuSet('test_baidu_set'))

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)