#!/usr/bin/env python
#coding=utf-8

import random
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import time
import random
from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType

def forgetPasswd(phone="",code=""):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1.2'
    desired_caps['deviceName'] = 'Lenovo P1c72'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['appPackage'] = 'com.android.mms'
    desired_caps['appActivity'] = '.ui.ConversationList'
    dd = webdriver.Remote('http://172.16.20.92:4723/wd/hub', desired_caps)
#    airplane_mode = ConnectionType.AIRPLANE_MODE
#    dd.set_network_connection(airplane_mode)
#    wifi_only = ConnectionType.WIFI_ONLY
#    dd.set_network_connection(wifi_only)
#    data_only = ConnectionType.DATA_ONLY
#    dd.set_network_connection(data_only)
#    all_network = ConnectionType.ALL_NETWORK_ON
#    dd.set_network_connection(all_network)
#    print dd.network_connection
    time.sleep(5)
    dd.find_element_by_accessibility_id('新建信息').click()
    dd.find_element_by_id('com.android.mms:id/mz_recipient_edit').send_keys('13112341234')
    sss = u"照哦姑娘问".encode('UTF-8')
    print sss
    dd.keyevent(3)
    dd.keyevent(26)
    dd.current_activity()
    dd.find_element_by_id('com.android.mms:id/embedded_text_editor').send_keys('hello')
    dd.find_element_by_id('com.android.mms:id/right_btn').click()
    time.sleep(1)
    desired_caps['appPackage'] = 'com.xueguex'
    desired_caps['appActivity'] = 'com.xueguoxue.MainActivity'
    dd = webdriver.Remote('http://172.16.20.92:4723/wd/hub', desired_caps)
    time.sleep(5)
    dd.quit()
    
if __name__ == "__main__":
#    plist = ["1","131123451234","","131123a456","!@#","``","''","$nbsp","13166666666","13112341234"]
    plist = [1]
    for i in plist:
        forgetPasswd(i,str(random.randint(10000,9999999)))
