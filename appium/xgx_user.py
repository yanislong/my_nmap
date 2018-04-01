#!/usr/bin/python
# -*- coding=utf-8 -*-

from appium import webdriver
import time

phone = {}
phone['platformName'] = "Android"
phone['platformVersion'] = '4.2.0'
phone['deviceName'] = "Meizu"
phone['unicodeKeyboard'] = True
phone['resetKeyboard'] = True
phone['appPackage'] = 'com.xueguex'
phone['appActivity'] = 'com.xueguoxue.MainActivity'

dd = webdriver.Remote('http://172.16.20.92:4723/wd/hub', phone)
w = dd.get_window_size()['width']
h = dd.get_window_size()['height']
time.sleep(5)
dd.find_element_by_name(u'我的').click()
dd.find_element_by_name(u'手机号').send_keys('13188888311')
dd.find_element_by_xpath('//android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.EditText').send_keys('123123')
dd.hide_keyboard()
time.sleep(1)
dd.find_element_by_name(u'登录').click()
time.sleep(1)
dd.find_element_by_name(u'我的').click()
time.sleep(2)
dd.find_element_by_name(u'我的订单').click()
time.sleep(1)
dd.swipe(w * 0.25, h * 0.5, w * 0.75, h * 0.5)
print "swipe"
time.sleep(1)
#dd.find_element_by_xpath('//android.widget.HorizontalScrollView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.ImageView').click()
time.sleep(3)
dd.quit()
