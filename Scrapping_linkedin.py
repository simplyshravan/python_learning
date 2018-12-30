import requests
from bs4 import BeautifulSoup
import json

file_in = r'C:\Users\Dell\Documents\idlinkedin.csv'
dataset = open(file_in, "r")

def login(iemail,ipassword):
    client = requests.Session()

    HOMEPAGE_URL = 'https://www.linkedin.com'
    LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'

    html = client.get(HOMEPAGE_URL).content
    soup = BeautifulSoup(html, "html.parser")
    csrf = soup.find(id="loginCsrfParam-login")['value']

    login_information = {
        'session_key': iemail,
        'session_password': ipassword,
        'loginCsrfParam': csrf,
    }

    client.post(LOGIN_URL, data=login_information)

    for username in dataset:
        item_url = 'https://www.linkedin.com/in/' + username.strip()
        print(item_url)
        source_code = client.get(item_url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for item_name in soup.find_all('code'):
            if str(item_name).find('firstName') > -1:
                for i in json.loads(item_name.text)['included']:
                    #print(i)
                    if len(i['$deletedFields']) > 0:
                        if i['$type']=='com.linkedin.voyager.identity.shared.MiniProfile':
                            if i["publicIdentifier"]==username.strip():
                                    print(i['firstName']+' '+i['lastName'])
                                    print(i['lastName'])
                                    print(i['occupation'])
                                    break

# MAIN
login('username','password')
