#! /usr/bin/env python
# coding=utf-8
import urllib2
import os
url = 'http://sample.heyzo.com/contents/3000/0733/heyzo_hd_0733_sample.mp4'
id = 733
urls = 'http://sample.heyzo.com/contents/3000/0%d/heyzo_hd_0%d_sample.mp4' %(id,id)
mp4 = urllib2.urlopen(urls)   
with open('sample.mp4','wb') as dat:
    dat.write(mp4.read())
print 'Downloading finished'
#os.system('mkdir tmp && cd tmp && unzip ~/peace_essay.ZIP')
#os.system('start winrar e c:\python27\peace_essay.ZIP')
#print 'Extracting finished'
raw_input("exit")
