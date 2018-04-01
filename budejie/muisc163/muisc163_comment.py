#!/usr/bin/python
# -*- coding=utf-8 -*-

import requests
import MySQLdb
import bs4
import re

class muiscComment():

    def __init__(self):
        self.sql = MySQLdb.connect(host='172.16.20.123',port=3306, user="long", passwd="123", db="muisc163", charset="utf8")
        print "mysql connect success"

    def getComment(self):
#        s = requests.Session()
        url = "http://music.163.com/weapi/v1/resource/comments/A_PL_0_634265582?csrf_token="
        header = {}
        header['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        data = {}
        data['params'] = "K/lYeS50tx0bl6MIPw4v/ca27r0Ki+SwKQrlfKrVm7AWcypcTIePgCUW4HbV21AVmdF9LZ/XDG1b+leCguA4K3txz1M3Oo8SoO48yfDOnhNLH23YJTtAQD/jP3ZQyBH6hbblZW5sH41ej4gA+xw7TPFo5OTmw0B2UQrmM0pAEO/NHHVIA5Pn/rL3c/jU8n3E"
        data['encSecKey'] = "8988c63e054234e0dc51e6086cb20edb23c47925f45f061819ad5e90699b25e3f176f20b3b56b50e5e85fb4e1fbeaf3d2bea0e4595c7dace23c016b27f4f5fd6b38e34ed1865a2f2d1cdac5b4d6893679b6a12cab9bac15715815c4be5f6d871bed80ab338cb058315365b42b2e46bc4ac6a3ec76fc134e7f9cc90bd508e6ecf"
        r = requests.post(url, headers=header, data=data)
#        print r.content
        l1 = re.findall(r'content":"(.*?)"',r.content)
        return l1
#        print l1
#        for i in l1:
#            print i
#        html = bs4.BeautifulSoup(r.content)
#        print html.find_all(_class="m-cmmtipt f-cb f-pr")
    
    def commentToDb(self):
        content = self.getComment()
        cur = self.sql.cursor()
        for i in content:
            cur.execute('insert into comment (content) value (%s)', i.decode(encoding="utf-8"))
        cur.close()
        self.sql.commit()

    def __del__(self):
        self.sql.close()
        print "mysql connect close"

if __name__ == "__main__":
    a = muiscComment()
    a.commentToDb()
#    a.getComment()
