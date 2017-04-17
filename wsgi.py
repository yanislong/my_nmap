#!/usr/bin/python
# -*- coding=utf-8 -*-

from wsgiref.simple_server import make_server

def application(environ, start_response):
    start_response('404 not', [('Content-type', 'text/html')])
    return [b'<h1>hello %s im hacker!!</h1>'% (environ['PATH_INFO'][1:] or 'web')]

httpd = make_server('', 9091, application)
print "Server HTTP on port 9091"
httpd.serve_forever()
