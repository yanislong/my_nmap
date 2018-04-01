#!/usr/bin/python
#-*-coding=utf-8-*-

import requests
import scrapy
from todayMoive.items import TodayMoiveItem

class wuHanMoiveSpider(scrapy.Spider):
    name = "jy"
    allowed_domains = ["wmpic.me"]
    start_urls = ["http://www.wmpic.me/tupian/qingxin/page/6"]

    def parse(self,response):
        subSelector = response.xpath('//div[@class="inner_item_box"]')
        print subSelector
        items = []
        for sub in subSelector:
            item = TodayMoiveItem()
            item['moiveName'] = sub.xpath('./h2/a/text()').extract()
            items.append(item)
        print 'end'
        return items

if __name__ == "__main__":
    pass
#    u = "http://www.jycinema.com/html/default/cinema.html"
    #r = requests.get(u)
#    p = r.content
#    long = wuHanMoiveSpider()
#    long.parse()
