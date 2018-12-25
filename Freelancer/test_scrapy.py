from Web_Scrapy_Project import getchildurls,getnoofpages,getdata
#import threading 
import datetime


print(datetime.datetime)
url='https://www.solekitchen.de/'

for i in getchildurls(url):
    print(i)
    if 'blog' in i:
        break;
    gnop=getnoofpages(i)
    getdata(i,gnop)
    #t1=threading.Thread(target=getdata, args=(i,gnop,))
    #t1.start()
    #t1.join()
    #break
