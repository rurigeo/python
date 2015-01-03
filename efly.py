#!/usr/bin/env python 
# coding=utf-8

import os
import re
import ConfigParser
import urllib2

CONFIG = ConfigParser.ConfigParser()
p = re.compile('efly.py')
CONFIG_FILENAME  = p.sub('proxy.ini', os.path.abspath(__file__))
print '.ini file path: {}'.format(CONFIG_FILENAME)

CONFIG.read([CONFIG_FILENAME])
ip = CONFIG.get('iplist','google_hk')
print ip

url = urllib2.urlopen('https://cb.e-fly.org/archives/goagent-iplist.html')

with open('html','w+') as tmp:
    tmp.write(url.read())
f = open('html')    
for line in f:
    if line.startswith('<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;"><a href='):
        s1 = re.search('a href.*.txt',line)
        s2 = re.search('\d{4}\/\d+\/\d{5,}',s1.group(0))
        s3 = 'https://cb.e-fly.org/usr/uploads/'+s2.group(0)
        print s3
        print 'ok'
        break
f.close()
url = urllib2.urlopen(s3)
update = url.read()
CONFIG.set('iplist','google_hk',update)
hosts = [x for x in CONFIG.get('iplist', 'google_hk').split('|') if not re.match(r'^\d+\.\d+\.\d+\.\d+$', x) and ':' not in x]
print 'extend_iplist start for hosts=%s' % hosts
CONFIG.write(open(CONFIG_FILENAME,'w'))
