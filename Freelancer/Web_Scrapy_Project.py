from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import json
 

def getchildurls(parenturl):
    listofurls=[]
    rooturl='https://www.solekitchen.de/'
    r=requests.get(rooturl);
    soup=BeautifulSoup(r.text,'lxml');
    listofurls=[ k.get('href') for k in soup.find('section').find_all('a') if k.get('class')[0]=='navigation--link' and re.match('^https+',k.get('href'))]
    return listofurls

   

def getnoofpages(url):
    getreq=requests.get(url+'?p=1&n=96');
    soup1=BeautifulSoup(getreq.text,'lxml');
    if soup1.find('strong')!=None:
        noofpages=int(soup1.find('strong').text)    
    else:
        noofpages=1
    return noofpages


def getdata(urllist,nop):
    z=0
    df=pd.DataFrame(columns=['ProductName','Description'])
    print(urllist)
    print(nop)
    for x in range(nop):
        getreq=requests.get(urllist+'?p='+str(x+1)+'&n=96');
        soup1=BeautifulSoup(getreq.text,'lxml');
        listofitemurls=list(set([ k.get('href') for k in soup1.find('section').find_all('a')   if k.get('class')!=None and k.get('class')[0]=='product--image' ]))
        print('start')
        for listofitemurl in listofitemurls:
            getreqitem=requests.get(listofitemurl);
            soup2=BeautifulSoup(getreqitem.text,'lxml');
            itemdescription=soup2.find('div',{'class':'product--description'}).text.strip()
            itemname=soup2.find('div',{'class':'content--title'}).text.strip()
            df=df.append({'ProductName':itemname,'Description':itemdescription},ignore_index=True)
            id=0
            dfstring=[]
            listofitemimage=list(set([ k.get('srcset') for k in soup2.find('section').find_all('img') if k.get('srcset')!=None ] ))
            for i in listofitemimage:
                for j in i.split(' '):
                    if j.endswith('.jpg'):
                        id=id+1
                        resp=requests.get(j)
                        fopen=open('images/'+j.split('/')[len(j.split('/'))-1],'wb')
                        fopen.write(resp.content)
                        fopen.close()
                        filename=r'external:images/'+j.split('/')[len(j.split('/'))-1]
                        dfstring.append('"Image'+str(id)+'" : "'+filename+'"')
                        k="{"+','.join(dfstring)+"}"
            if z==0:
                df1=pd.DataFrame(json.loads(k),index=[z])
            else:
                df1=df1.append(pd.DataFrame(json.loads(k),index=[z]))
            z=z+1
        #break
    df2=pd.concat([df,df1],axis=1,join_axes=[df1.index])
    writer = pd.ExcelWriter('pandas_image.xlsx', engine='xlsxwriter')
    df2.to_excel(writer, sheet_name=urllist.split('/')[-1])
    writer.save()
    print('exit')
    return 'Please check filename pandas_image.xlsx'




