import subprocess
import os
import xml.etree.ElementTree as ET
import csv
import pandas as pd

svn_data = open('Jan30_Data.csv', 'w', newline='')
csvwriter = csv.writer(svn_data)
list1=[]
for commsg in open(os.getcwd()+'\Jan30_commit_messages.txt'):
    filelist=''
    cmd1='svn log -v --search "'+commsg.strip()+'" SVN_URL --xml'
    list1=[]
    k=subprocess.Popen(cmd1,stdout=subprocess.PIPE, shell=True)
    output,errors=k.communicate()
    p_status = k.wait()
    root = ET.fromstring(str(output,'utf-8'))
    for item in root.findall('./logentry/paths/'):
        len1=len(item.text.split('/'))
        comp_path='/'.join(item.text.split('/')[len1-2:len1])
        if comp_path not in list1:
            list1.append(comp_path)
        else:
            continue
    csvwriter.writerow([commsg.strip(),'\n'.join(list1)])

svn_data.close()
