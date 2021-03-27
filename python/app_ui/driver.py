# -*- coding: UTF-8 -*-

from appium import webdriver
import time

APPIUM_LOCAL_HOST_URL = 'http://localhost:4723/wd/hub'


class Driver(object):
    # 初始化driver
    def __init__(self):
        config = {
            'platformName': 'iOS',
            'platformVersion': '10.4',
            'deviceName': 'xxx',
            'app': 'xxx'
        }
        self.driver = webdriver.Remote(APPIUM_LOCAL_HOST_URL, config)

    def get_driver(self):
        time.sleep(2)
        return self.driver
