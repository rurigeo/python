#! /usr/bin/env python
# coding=utf-8
import urllib2
response = urllib2.urlopen('http://www.nod32jihuoma.cn/')
html = response.read()
with open('test','wb') as f : f.write(html)
f = open('test','rb')
for line in f:
    #print line.decode('utf-8').rstrip()
    if line.rstrip().startswith('<p>用户名'):
        print line.rstrip()
        user = line.rstrip()[15:31]
        passwd = line.rstrip()[48:58]
        print 'user:%s\npassword:%s' %(user,passwd)
        break
print 'ok'
dlurl = 'wget http://download.eset.com/download/engine/eav/offline_update_eav.zip \
--http-user=%s --http-passwd=%s' %(user,passwd)
os.system(dlurl)
