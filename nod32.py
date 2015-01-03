#! /usr/bin/env python
# coding=utf-8
import urllib2
response = urllib2.urlopen('http://www.nod32jihuoma.cn/')
html = response.read()
with open('c:\\test','wb') as f : f.write(html)
f = open('c:\\test','rb')
for line in f:
    #print line.decode('utf-8').rstrip()
    if line.rstrip().startswith('<p>用户名'):
        print line.rstrip()
        break
