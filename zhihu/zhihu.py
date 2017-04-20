#!/usr/bin/python
# -*- coding=utf-8 -*-

import requests
import bs4

def re_href():
    u = "http://www.zhihu.com"
    s = ""
    url = "https://www.zhihu.com/topic/19550874/hot"
    header = {}
    header['cookie'] = """q_c1=45e48bbfe47a4b409f00971ba88d9f23|1490331402000|1490331402000; capsion_ticket="2|1:0|10:1492052235|14:capsion_ticket|44:YTRiY2NiNzFhZGZiNGVjMGE2N2NmMjJmZDRiZTNlZjY=|1ae8cffadd001b9fbbe750ced378d0347d9446540ff73d2ec14fcc9f588f9914"; aliyungf_tc=AQAAAAIZclPGHwgAdhyHPR5baPACHgMj; d_c0="ACBC6clToguPTsqY5c9ttjHwylYGtsd22XM=|1492652161"; _xsrf=29049dc835a67a669984783556f818d0; _zap=9daebc3f-9bb3-4856-ac5c-441d8054866f; s-q=%E5%B0%84%E5%BD%B1; s-i=3; sid=gah569lo; s-t=autocomplete; r_cap_id="N2IwNjFmYTQ5NThhNGMwYThiZDY4MjIxNmY5MWNlNDg=|1492653597|41e1b08019850fa18259b975969487eaf1685206"; cap_id="NzM2NTE5MGJlYTBmNGI0MWEwMmFhYTMyYjYwZDIxYWI=|1492653597|3afde6249c6b9d6575ab94cfa4068d85c7308b1a"; l_n_c=1; __utma=51854390.131887152.1492652180.1492652180.1492652180.1; __utmb=51854390.0.10.1492652180; __utmc=51854390; __utmz=51854390.1492652180.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/20039623; __utmv=51854390.100-1|2=registration_date=20170420=1^3=entry_date=20170324=1; z_c0=Mi4wQUpDQ2l6VlVvZ3NBSUVMcHlWT2lDeGNBQUFCaEFsVk5ScU1mV1FEa0loWHFyOU1xWUpJQ0xFbUJnWFlGWV9TQndn|1492653685|89fd056f5822026c58a9e7be12659eaa75d2526e"""
    header['X-Requested-With'] = "XMLHttpRequest"
    header['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
    header['X-Xsrftoken'] = "29049dc835a67a669984783556f818d0"
    r = requests.get(url, headers=header)
    html = bs4.BeautifulSoup(r.content)
    tt = html.find_all(class_="zu-main-content-inner")
    for i in tt:
        for j in i.contents:
            if type(j) == bs4.element.Tag:
                t2 = j.find_all(class_="question_link")
                for k in t2:
                    s1 = ""
                    s1 = u + k['href']
                    print s1
                    r1 = requests.get(s1, headers=header)
                    html1 = bs4.BeautifulSoup(r1.content)
                    title = html1.find(class_="QuestionHeader-title")
                    content = html1.find(class_="RichText")
                    content1 = html1.find(class_="RichText CopyrightRichText-richText")
                    print title.string
                    print content1
#                    print content.string

re_href()

