# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time

class TodaymoivePipeline(object):
    def process_item(self, item, spider):
        now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        fileName = "wuhan" + now + ".txt"
        with open(fileName,'a') as f:
            ss = item['moiveName'][0].strip()
            f.write(ss.encode('utf8') + "\n\n")
        return item
