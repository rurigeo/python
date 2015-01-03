import urllib2
import os
print os.path.abspath(__file__)
print os.path.realpath(__file__)
try:
    response = urllib2.urlopen('http://www.riverbankcomputing.com/static/Docs/PyQt4/html/classes.html')
#except IOError, e:
#except urllib2.HTTPError, e:
except urllib2.HTTPError as e:    
    print e.code
    print e.reason
raw_input('Press ENTER to EXIT')