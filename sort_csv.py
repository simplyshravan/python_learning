import csv
import json

data = csv.reader(open('sample.csv'))
import operator
sortedlist = sorted(data, key=operator.itemgetter(2), reverse=False)

for i in sortedlist:
    print(i)
