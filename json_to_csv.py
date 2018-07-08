import json
import csv
from pprint import pprint

#with open('sample.json') as data_file:
#    data = json.loads(data_file.read())

#print(data)

json_file='sample.json'  #getting the json file input
json_data=open(json_file) #openning json file
data = json.load(json_data) #loading json file into string innput to data variable
#so data will be a list with comma seprated values and key value pair storage as we have in python
#print(data)

#print("signOffDate,fundEntityType,fundId,benchmarkIds,source,returnType") # printing headers of csv
for item in data: #items in data is key:value pair 
    print(item.values()) #to access all values in each key:value pair
    print(item.keys()) #to access all keys in each key:value pair
    #print (item['signOffDate'],item['fundEntityType'],item['fundId'],item['benchmarkIds'],item['source'],item['returnType'])

#Now code for creating csv
# open a file for writing
employ_data = open('Data.csv', 'w')
# create the csv writer object
csvwriter = csv.writer(employ_data)
count = 0
for emp in data:
    if count == 0:
             header = emp.keys()
             csvwriter.writerow(header)
             count += 1
    csvwriter.writerow(emp.values())
employ_data.close()
