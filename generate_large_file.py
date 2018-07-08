outfile = open('file_with_dup.csv', "w")
for i in range(1,100):
    line=str(i+1)+','+str(i+2)+','+'Abcngh'+str(i+3)+','+str(i+4)+','+str(i+5)+','+str(i+6)+'\n'
    outfile.write(line)
outfile.close
