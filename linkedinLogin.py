import requests
from bs4 import BeautifulSoup

s = requests.session()
r = s.get('https://www.linkedin.com/uas/login')
soup = BeautifulSoup(r.text, "lxml")
loginCsrfParam = soup.find('input', {'name':'loginCsrfParam'})['value']
#print('loginCsrfParam: '+loginCsrfParam)
csrfToken = soup.find('input', {"name" : 'csrfToken'})['value']
#print('csrfToken: '+csrfToken)
sourceAlias = soup.find('input', {'name':'sourceAlias'})['value']
#print('sourceAlias: '+sourceAlias)

payload = {
'session_key': 'your email address',
'session_password': 'your password',
'loginCsrfParam' : loginCsrfParam,
'csrfToken' : csrfToken,
'sourceAlias' : sourceAlias
}


s.post('https://www.linkedin.com/uas/login-submit', data=payload)
loggedSoup = BeautifulSoup(s.get('http://www.linkedin.com/nhome').text, "lxml")
name = loggedSoup.find('img', {'class':'img-defer-hidden img-defer nav-profile-photo'})['alt']
print(name + " just logged in...")