import urllib2
req = urllib2.Request(url='http://go.microsoft.com/fwlink/?linkid=140813'
                      #,data='This data is passed to stdin of the CGI'
                      )
f = urllib2.urlopen(req)
print f.read()
