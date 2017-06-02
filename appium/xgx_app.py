#!/usr/bin/env python
#coding=utf-8

import random
import sys
import os
import time
from appium import webdriver

#width = dd.get_window_size()['width']
#height = dd.get_window_size()['height']

def login(name,passwd):
    global desired_caps
    dd = webdriver.Remote('http://172.16.20.92:4723/wd/hub', desired_caps)
    time.sleep(5)
    dd.get_screenshot_as_file(r'/root/Desktop/app_tu/test.png')
    dd.find_element_by_name(u'手机号').send_keys(name)
    tt = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime())
    dd.get_screenshot_as_file(r'/root/Desktop/app_tu/' + tt + ".png")
    dd.find_element_by_xpath('//android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.EditText').send_keys(passwd)
    dd.hide_keyboard()
    time.sleep(1)
#    dd.tap([(150,668), (570, 758)], 200)
    dd.find_element_by_name(u'登录').click()
    time.sleep(3)
#    num = str(random.random())
    dd.get_screenshot_as_file('/root/Desktop/app_tu/test1.png')
    content2 = dd.find_element_by_name(name).get_attribute('text')
    content3 = dd.find_element_by_xpath('//android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.EditText').get_attribute('text')
    print content2
    print content3
    dd.find_element_by_xpath("//android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.EditText").click()
    for i in range(0,len(content3)):
        dd.keyevent(67)
    dd.find_element_by_name(content2).click()
    dd.keyevent(123)
    for j in range(0,len(content2)):
        dd.keyevent(67)
        time.sleep(1)
    dd.quit()

def forget_passwd():
    dd = webdriver.Remote('http://172.16.20.92:4723/wd/hub', desired_caps)
    time.sleep(5)
    dd.find_element_by_name(u'忘记密码').click()
    time.sleep(2)
    dd.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText').send_keys('13141032576')
    dd.find_element_by_name(u'发送验证码').click()
    dd.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.EditText').send_keys('131410')
    dd.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.widget.EditText').send_keys('1314103257a6')
    dd.find_element_by_name(u'确定').click()
    dd.hide_keyboard()
    time.sleep(2)
    dd.get_screenshot_as_file(r'/root/Desktop/long.png')
    dd.quit()

def register():
    global desired_caps
    dd = webdriver.Remote('http://172.16.20.92:4723/wd/hub', desired_caps)
    time.sleep(5)
    dd.find_element_by_name(u'注册').click()
    time.sleep(2)
    dd.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText').send_keys('13141032576')
    dd.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.EditText').send_keys('131410')
    dd.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.widget.EditText').send_keys('032576')
    dd.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.widget.EditText').send_keys('a13141032576')
    dd.hide_keyboard()
    dd.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[6]/android.widget.ImageView').click()
    time.sleep(3)
    dd.find_element_by_name(u'快速注册').click()
    time.sleep(2)
    dd.get_screenshot_as_file(r'/root/Desktop/long.jpg')
    dd.quit()

if __name__ == "__main__":
    try:
        parme = [['long','123123'],['gege','000000'],['13100000000','xxxxxx']]
        for i in range(1):#parme:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1.2'
            desired_caps['deviceName'] = 'Lenovo P1c72'
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True
            desired_caps['appPackage'] = 'com.xueguex'
            desired_caps['appActivity'] = 'com.xueguoxue.MainActivity'
#            desired_caps['app'] = r'C:\Users\huang\Downloads\app-release.apk'
            time.sleep(1)#启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然>下面>会一直报错定位不到元素
#        forget_passwd()
#        for i in parme:
#        dd = webdriver.Remote('http://172.16.20.92:4723/wd/hub', desired_caps)
#        dd.get_screenshot_as_file('/root/Desktop/long.png')
#        register()
        login('123',123)
#        login(i[0],i[1])
    except ValueError:
        print 'error quit'
        dd.quit()
    finally:
        print '>>quit!'
