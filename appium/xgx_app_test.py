#!/usr/bin/env python
#coding=utf-8

import random
import re
import sys
import os
import time
import random
from appium import webdriver

def forgetPasswd(phone="",code=""):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1.2'
    desired_caps['deviceName'] = 'Lenovo P1c72'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['appPackage'] = 'com.xueguex'
    desired_caps['appActivity'] = 'com.xueguoxue.MainActivity'
    dd = webdriver.Remote('http://172.16.20.92:4723/wd/hub', desired_caps)
    time.sleep(5)
    dd.find_element_by_name(u'忘记密码').click()
#    time.sleep(1)
#    tt = time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime())
#    dd.get_screenshot_as_file(r'/root/Desktop/forgetpw/' + tt + '.png')
    dd.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText').send_keys(phone)
    dd.find_element_by_name(u'发送验证码').click()
    time.sleep(1)
    tt = time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime())
    if re.findall(r'^\d{11}$',phone):
        dd.get_screenshot_as_file(r'/root/Desktop/forgetpw/activePhone/' + tt + '.png')
    else:
        dd.get_screenshot_as_file(r'/root/Desktop/forgetpw/invalidPhone/' + tt + '.png')
    dd.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.EditText').send_keys(code)
    time.sleep(1)
    tt = time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime())
    if re.findall(r'\d{6}',code):
        dd.get_screenshot_as_file(r'/root/Desktop/forgetpw/activeCode/' + tt + '.png')
    else:
        dd.get_screenshot_as_file(r'/root/Desktop/forgetpw/invalidCode/' + tt + '.png')
    dd.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.widget.EditText').send_keys('1314103257a6')
#    time.sleep(1)
#    tt = time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime())
#    dd.get_screenshot_as_file(r'/root/Desktop/forgetpw/' + tt + '.png')
    dd.find_element_by_name(u'确定').click()
#    time.sleep(1)
#    tt = time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime())
#    dd.get_screenshot_as_file(r'/root/Desktop/forgetpw/' + tt + '.png')
    dd.quit()

if __name__ == "__main__":
    plist = ["1","131123451234","","131123a456","!@#","``","''","$nbsp","13166666666","13112341234"]
    for i in plist:
        forgetPasswd(i,str(random.randint(10000,9999999)))
