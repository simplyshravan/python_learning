from bs4 import BeautifulSoup
import requests
import urllib
import json
import pandas as pd
from datetime import datetime
 
#print(datetime.fromtimestamp(1287225997)) DATE OF LAST POST
#mylist=list(("a b c d e f g h i j k l m n o p q r s t u v w x y z").split())
listofurls=[]
#print(mylist)
#for i in range(21):
#    if i+6 > 25:
#        i=i-19
#    listofurls.append('http://www.instagram.com/'+''.join(mylist[i:i+6]))

from nltk.corpus import words
word_list = words.words()
j=0
for i in word_list:
    listofurls.append('http://www.instagram.com/'+i)
    j=j+1
    if j >100:
        break;    

print(listofurls)
#listofurls='http://www.instagram.com/shravan'

#listofurls=['https://www.instagram.com/aaron/']
df=pd.DataFrame(columns=['Username','is_private','biography','external_url','Followers','Following','Posts','Profile_pic','Profile_pic_hd'])
#print(df)
#i=0
#i=i+1
   # if i==100:
        #break;
for url in listofurls:
    r=requests.get(url);
    soup=BeautifulSoup(r.text,'lxml');
    metatag1=soup.find('title')
    if metatag1.get_text().strip()!='Page Not Found • Instagram':         
        username=(metatag1.get_text().split(')')[0]+')').replace('\n','')
        metatag=soup.find_all('meta',{'name':'description'})
        desc=metatag[0]['content'].split(',');
        for i in desc:
            if str(i).find('Followers') > -1:
                followers=str(i).split()[0]
            if str(i).find('Following') > -1:
                following=str(i).split()[0]
            if str(i).find('Posts') > -1:
                posts=str(i).split()[0]
        metatag2=soup.find_all('meta',{'property':'og:image'})
        profile_pic=metatag2[0]['content']
        metatag3=soup.find_all('script',{'type':'text/javascript'})
        for i in metatag3:
            for k in i:
                if (str(k).find('window._sharedData')) > -1:
                    for x in k.split(' = {'):
                        if not x is None:
                            if str(x).find('{') > -1:
                                print(username);
                                print('#####'+x)
                                xy=json.loads('{'+str(x).split(':true};')[0]+':true}')
                            #xy=json.loads(str(x)+'"}}]}}}}]}}')
                            #xy=json.loads(str(x)+'"}}}]}}')
                            #print(xy.keys())
                            #print(xy['country_code'])
                                biography=xy['entry_data']['ProfilePage'][0]['graphql']['user']['biography']
                                external_url=xy['entry_data']['ProfilePage'][0]['graphql']['user']['external_url']
                                is_private=xy['entry_data']['ProfilePage'][0]['graphql']['user']['is_private']
                                profile_pic_hd=xy['entry_data']['ProfilePage'][0]['graphql']['user']['profile_pic_url_hd']
    df=df.append(pd.Series([username,is_private,biography,external_url,followers,following,posts,profile_pic,profile_pic_hd],index=['Username','is_private','biography','external_url','Followers','Following','Posts','Profile_pic','Profile_pic_hd']),ignore_index=True)
        #logging_page_id

#print(df)    
#df=df.append(pd.Series([username,is_private,biography,external_url,followers,following,posts,profile_pic,profile_pic_hd],index=['Username','is_private','biography','external_url','Followers','Following','Posts','Profile_pic','Profile_pic_hd']),ignore_index=True)
df.to_csv(r"C:\Users\DELL\Documents\my.csv");
#print(metatag[0]['content'].split(','))

#metatag1=soup.find('title')
#print(metatag1.get_text().split(')')[0]+')')
    

    

    