import datetime

print(datetime.datetime.now()) # to print date time in python

#the solution is good for file size beyond. It has also limitations. depends on your RAM usage
lines_seen = set() # holds lines already seen. set() function also hold unique list of rows always. So the output file here as sorted data**
outfile = open('file_without_dup.csv', "w")  # opening an outfile in write mode
for line in open('file_with_dup.txt', "r"): # reading the input file
    if line not in lines_seen: # checking if the input file record exits in new lines_seen variable
        outfile.write(line) #if the record does not exit in lines_seen variable then write that in output file
        lines_seen.add(line) # add the new record in lines_seen variable**
outfile.close() # closing new file created

print(datetime.datetime.now())  # to print date time in python

# the below solution is good for smaller file size. upto 300mb or 400mb file only. Beyond that it will give you Memory error.
uniqlines = set(open('file_with_dup.txt').readlines()) #create variable which contains the reocrds returned by set function
bar = open('file_without_dup2.csv', 'w').writelines(uniqlines) # writing those records in output file  but it does not sort the data in output file. Not even this--> bar = open('file_without_dup2.csv', 'w').writelines(set(uniqlines))
#bar.close()
##print(uniqlines)

print(datetime.datetime.now())
