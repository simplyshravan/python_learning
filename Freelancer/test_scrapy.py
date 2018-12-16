from Web_Scrapy_Project import getchildurls,getnoofpages,getdata


url='https://www.solekitchen.de/'

for i in getchildurls(url):
    print(i)
    if 'blog' in i:
        break;
    print(getnoofpages(i))


