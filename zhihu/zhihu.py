#!/usr/bin/python
# -*- coding=utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('/root/git_20170207/wenzhang')
import zhihu1
import chardet
import re
import requests
import bs4
import json

def re_href():
    global header
    u = "http://www.zhihu.com/"
    s = ""
#    url = "https://www.zhihu.com/topic/19550874/hot"
    url = "https://www.zhihu.com/node/TopStory2FeedList"
    header['X-Requested-With'] = "XMLHttpRequest"
    header['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
    header['Referer'] = "https://www.zhihu.com/"
    header['X-Xsrftoken'] = "55ae7012f80897f5f3e38a2fdfafb24b"
    data = {}
    data['params'] = json.dumps({'offset':63,"start":"9"})
    data['method'] = "next"
    r = requests.post(url, headers=header, data=data)
    a = r.content.replace('\n',"")
    b = a.replace('\\',"")
#    print b
#    print chardet.detect(r.content[0:2000])
#    l1 = r.content.decode('utf8')
#    print chardet.detect(l1)
    l2 = re.findall(r'href="https://(.*?)"',b, re.MULTILINE)
    l3 = re.findall(r'href="/(.*?)"',b)
    l4 = list(set(l2))
    l5 = list(set(l3))
#    print l4
#    print l5
#    html = bs4.BeautifulSoup(r.content)
#    tt = html.find_all(class_="zu-main-content-inner")
    for i in l4:
        i = "http://" +i
        print i
        r1 = requests.get(i, headers=header)
        html1 = bs4.BeautifulSoup(r1.content)
        title = html1.find(class_="QuestionHeader-title")
        content = html1.find(class_="RichText")
        content1 = html1.find(class_="RichText CopyrightRichText-richText")
        try:
#            print title.string
#            print content1
            zhihu1.send(title.string,content1)
        except AttributeError:
            print "no have title or content"

    for j in l5:
        j = u + j
        print j
        if "topic" in j:
            print 'jinlai le '
            j = j + "/hot"
            zhihu1.re_href(j)
            continue
        else:
            r1 = requests.get(j, headers=header)
        html1 = bs4.BeautifulSoup(r1.content)
        title = html1.find(class_="QuestionHeader-title")
        content = html1.find(class_="RichText")
        content1 = html1.find(class_="RichText CopyrightRichText-richText")
        try:
#            print title.string
#            print content1
            zhihu1.send(title.string,content1)
        except AttributeError:
            print "no have title or content"

        for j in []:#i.contents:
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


#url = "https://www.zhihu.com/people/li-zong-wu-44/activities"
header = {}
header['cookie'] = "capsion_ticket=2|1:0|10:1492052235|14:capsion_ticket|44:YTRiY2NiNzFhZGZiNGVjMGE2N2NmMjJmZDRiZTNlZjY=|1ae8cffadd001b9fbbe750ced378d0347d9446540ff73d2ec14fcc9f588f9914; _zap=9daebc3f-9bb3-4856-ac5c-441d8054866f; q_c1=d77705eb64a940b4a9d32d48cf7f8c4f|1492669207000|1492669207000; r_cap_id=YTA1ZGUyMDViNzU0NDJiMzk4YjY3ZTdlYmE2MGYyNjI=|1492669207|427e02080fa0b694dd10f203274986e0c1a71010; cap_id=ODg3Yjg0NmQyMTUxNGQxOWE2MWFkMzhkZGE2MWQxNjU=|1492669207|043c47c98b540ebb6fea7ad444146b071162bf46; _xsrf=55ae7012f80897f5f3e38a2fdfafb24b; d_c0=ACCCB4ePowuPThj85ovbLyYifCxn3QseubI=|1492734930; aliyungf_tc=AQAAAEJbVVS5jQwAdhyHPXzoPVm6ZwCk; acw_tc=AQAAADoUqhf6OA8AdhyHPeixixulj2SB; z_c0=Mi4wQUpDQ2l6VlVvZ3NBSUVMcHlWT2lDeGNBQUFCaEFsVk5PT0FmV1FCN091TmdzY05hcFFFQXFuaGJFWGFLREY5UE53|1493013343|895742c201ad2e0ab9ee4407f9d8fd11e7f7b019; __utma=51854390.398938069.1492670822.1492734946.1493013362.6; __utmb=51854390.0.10.1493013362; __utmc=51854390; __utmz=51854390.1493013362.6.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.100-1|2=registration_date=20170420=1^3=entry_date=20170420=1"
header['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"

re_href()
