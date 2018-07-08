import csv
import json
import pprint

with open("sample.csv", "r") as csvfile:  #started raeding csv file
    reader = csv.DictReader(csvfile) #reading the dictionary i.e. header as properties
    field = reader.fieldnames # getting field names
    csv_rows = [] # creating blank list
    for row in reader:
        csv_rows.append({field[i]:[row[field[i]]] if field[i]=='benchmarkIds' or  field[i]=='fundId' else row[field[i]] for i in range(len(field))})

#for i in csv_rows: 
#    pprint.pprint(i) # it will print the key and values in enclosed in single quotes. (which is not json recommended)

print(json.dumps(csv_rows)) ## it will print the key and values in enclosed in double quotes in single line
