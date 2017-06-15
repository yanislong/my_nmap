#!/usr/bin/python
#-*- coding=utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_id('')
driver.find_element_by_class_name('')
driver.find_element_by_tag_name('')
driver.find_element_by_xpath('//input[@id="123"]')
driver.quit()
