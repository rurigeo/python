import urllib2
# Create an OpenerDirector with support for Basic HTTP Authentication...
auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password(realm='ESET NOD32 Antivirus',
                          uri='http://download.eset.com/download/engine/eav',
                          user='TRIAL-0126140629',
                          passwd='bhakcpnbv8')
opener = urllib2.build_opener(auth_handler)
# ...and install it globally so it can be used with urlopen.
urllib2.install_opener(opener)
f=urllib2.urlopen('http://download.eset.com/download/engine/eav/offline_update_eav.zip')
print f.read()
