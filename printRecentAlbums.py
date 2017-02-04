import json
from pprint import pprint
from sys import argv

jsonFile = argv[1]

with open(jsonFile) as data_file:
    data = json.load(data_file)

for i in range(0, data['resultCount']):
    if data['results'][i]['trackCount'] != 1:
        pprint(data['results'][i]['collectionName'])


