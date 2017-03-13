import json
import time
from urllib2 import urlopen
from sys import argv

albumID = argv[1]

urlpath = urlopen('https://itunes.apple.com/lookup?id=' + albumID)

result = json.loads(urlpath.read())

print (result['resultCount'])

count = 0

while result['resultCount'] == 0:
    urlpath = urlopen('https://itunes.apple.com/lookup?id=' + albumID)
    result = json.loads(urlpath.read())
    print count, (result['resultCount'])
    count = count + 1
    time.sleep(4)

print 'Done'
