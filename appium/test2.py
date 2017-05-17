#!/usr/bin/env python
#coding=utf-8

import sys
import os
import time
#import unittest
from appium import webdriver
#from lib2to3.pgen2.driver import Driver
#from lib2to3.tests.support import driver
PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.2'
desired_caps['deviceName'] = 'Lenovo P1c72'
desired_caps['app'] = PATH(r'C:\Users\huang\Downloads\com.aixuetang.online_2.2.0_163.apk')

#desired_caps['appPackage'] = 'com.aixuetang.online'
#desired_caps['appActivity'] = 'com.aixuetang.mobile.activities.HomeActivity'
#如果设置的是app在电脑上的路径，则不需要配appPackage和appActivity，同理反之

dd = webdriver.Remote('http://172.16.20.92:4723/wd/hub', desired_caps)
print dir(dd)
#sys.exit()
time.sleep(10)#启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
width = dd.get_window_size()['width']
height = dd.get_window_size()['height']
#dd.swipe(width * 3 / 4, height / 2, width / 4, height / 2, 200)
time.sleep(3)
#driver.find_element_by_id('com.aixuetang.online:id/fixed_bottom_navigation_icon').click()
dd.find_element_by_name(u'选课').click()
time.sleep(2)
dd.find_element_by_name(u'我').click()
time.sleep(2)
dd.find_element_by_name(u'我的课程').click()
time.sleep(2)
dd.find_element_by_id('com.aixuetang.online:id/et_username').send_keys('yanislong')
time.sleep(2)
dd.find_element_by_id('com.aixuetang.online:id/et_password').send_keys('123456a~')
time.sleep(2)
dd.find_element_by_id('com.aixuetang.online:id/tv_login').click()
time.sleep(4)
dd.find_element_by_id('com.aixuetang.online:id/clcik_cancel').click()
time.sleep(2)
dd.find_element_by_name(u'设置').click()
time.sleep(2)
dd.find_element_by_name(u'退出当前账号').click()
time.sleep(2)

print '>>quit!'
dd.quit()
'''
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
import os
browser = webdriver.Chrome()
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"  
os.environ["webdriver.chrome.driver"] = chromedriver  
browser = webdriver.Chrome(chromedriver)  
url = "http://www.xueguoxue.com"  
browser.get("http://www.baidu.com")
'''

