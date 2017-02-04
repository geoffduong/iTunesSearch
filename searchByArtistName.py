import json
from urllib2 import urlopen
from sys import argv

if len(argv) == 1:
    sys.exit("Please enter artist name as arg")
artistName = argv[1]

for i in range(2, len(argv)):
    artistName = artistName + ' ' + argv[i]

artistName = '+'.join(artistName.split(' '))
print 'Artist name entered: ' + artistName

print 'Searching...'
urlpath = urlopen('https://itunes.apple.com/search?term=' + artistName + '&entity=album&limit=5&sort=recent')

target = open('artistJSON.json', 'w')
target.truncate()
print 'Writing JSON to text file...'
target.write(urlpath.read())
target.close()
print 'Done!'
