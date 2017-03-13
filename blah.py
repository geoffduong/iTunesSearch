import json
import time
from urllib2 import urlopen
from sys import argv

albumID = argv[1]

urlpath = urlopen('https://itunes.apple.com/lookup?id=' + albumID)

target = open('blah.json', 'w')
target.truncate()
target.write(urlpath.read())
target.close()

with open('blah.json') as data_file:
    data = json.load(data_file)

print (data['resultCount'])

count = 0

while data['resultCount'] == 0:
    urlpath = urlopen('https://itunes.apple.com/lookup?id=' + albumID)

    target = open('blah.json', 'w')
    target.truncate()
    target.write(urlpath.read())
    target.close()
    with open('blah.json') as data_file:
        data = json.load(data_file)

    print count, (data['resultCount'])
    count = count + 1
    time.sleep(4)

print 'IT IS OUTTTTT'
