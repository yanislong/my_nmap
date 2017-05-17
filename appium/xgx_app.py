#!/usr/bin/env python
#coding=utf-8

import sys
import os
import time
from appium import webdriver

#width = dd.get_window_size()['width']
#height = dd.get_window_size()['height']

def login(name,passwd):
    try:
        dd.find_element_by_name(u'手机号').send_keys(name)
    except:
        dd.find_element_by_name(name).send_keys(name)
    time.sleep(1)
    try:
        dd.find_element_by_name(u'密码').send_keys(passwd)
    except:
        dd.find_element_by_name(passwd).send_keys(name)
    #dd.hide_keyboard()
    time.sleep(1)
    dd.find_element_by_name(u'登录').click()
    time.sleep(1)
    content2 = dd.find_element_by_name(name).get_attribute('text')
    content3 = dd.find_element_by_name(passwd).get_attribute('text')
    print content2
    print content3
#    dd.keyevent(123)
    for i in range(0,len(content3)):
        dd.keyevent(67)
    dd.find_element_by_name(content2).click()
    for j in range(0,len(content2)):
        dd.keyevent(67)
    time.sleep(1)

def forget_passwd():
    dd.find_element_by_name(u'忘记密码').click()
    time.sleep(2)
    dd.find_element_by_name(u'返回').click()

def regiest():
    time.sleep(2)
    dd.find_element_by_name(u'注册').click()
    time.sleep(2)
    dd.find_element_by_name(u'返回').click()
    time.sleep(2)

if __name__ == "__main__":
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1.2'
    desired_caps['deviceName'] = 'Lenovo P1c72'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['app'] = r'C:\Users\huang\Downloads\app-release.apk'
    dd = webdriver.Remote('http://172.16.20.92:4723/wd/hub', desired_caps)
    time.sleep(5)#启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面>会一直报错定位不到元素
    parme = [['long','123123'],['gege','000000'],['13100000000','xxxxxx']]
    for i in parme:
        login(i[0],i[1])
    dd.quit()
    print '>>quit!'
