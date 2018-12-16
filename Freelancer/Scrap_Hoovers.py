from bs4 import BeautifulSoup
import requests

rooturl='http://www.hoovers.com/company-information/company-search.html'
with requests.Session() as se:
    se.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en"
    }
    resp = se.get(rooturl)
print(resp.content)
soup = BeautifulSoup(resp.content,"html.parser")