#! /user/bin/env python
# -*- coding:utf-8 -*-

from appium import webdriver
import time

APPIUM_LOCAL_HOST_URL = 'http://localhost:4723/wd/hub'


class Driver(object):
    # 初始化driver
    driver = None

    @classmethod
    def init_driver(cls):
        config = {
            'platformName': 'iOS',
            'platformVersion': '10.4',
            'deviceName': 'xxx',
            'app': 'xxx'
        }
        if cls.driver is None:
            cls.driver = webdriver.Remote(APPIUM_LOCAL_HOST_URL, config)
        time.sleep(2)
        return cls.driver
