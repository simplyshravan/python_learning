from bs4 import BeautifulSoup
#import requests
from selenium import webdriver

#options = webdriver.ChromeOptions()
#options.add_argument('--ignore-certificate-errors')
#options.add_argument("--test-type")
#options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
browser = webdriver.Chrome("E:\GitHub\python_learning\Freelancer\chromedriver_win32\chromedriver.exe")
browser.get('http://www.hoovers.com/company-information/company-search.html')

r = browser.page_source
print('hi1')
soup=BeautifulSoup(r,"html.parser")
print('hi2')
print(soup)

browser.close() 