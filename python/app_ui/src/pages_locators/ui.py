#! /user/bin/env python
# -*- coding:utf-8 -*-

from python.app_ui.src.pages_locators.baidu_home_page import baidu_home_page
from python.app_ui.src.pages_locators.baidu_search_results_page import baidu_search_results_page
from python.app_ui.src.pages_locators.baidu_login_in_page import baidu_login_in_page

ui = {
    "百度首页": baidu_home_page,
    "百度登录页": baidu_login_in_page,
    "百度搜索结果页": baidu_search_results_page
}