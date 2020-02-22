import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

def parceSite(url):
    r = requests.get(url)
    page = BeautifulSoup(r.text, 'html.parser')
    handle = open('test.txt', 'w')
    for i in page.findAll('a', href=True):
             if (i['href'][0:4] == "http"):
                 try:
                     response = urlopen(i['href'])
                 except HTTPError as e:
                     print(i['href']+': The server couldn\'t fulfill the request.')
                     print('Error code: ', e.code)
                     handle.write(i['href']+'\n')
                 except URLError as e:
                     print(i['href']+ ': We failed to reach a server.')
                     print('Reason: ', e.reason)
                     handle.write(url + i['href'] + '\n')
                 else:
                     print(i['href']+ ': Website is working fine')
             else:
                 try:
                     response = urlopen(url+i['href'])
                 except HTTPError as e:
                     print(url+i['href']+  ': The server couldn\'t fulfill the request.') # оно
                     print('Error code: ', e.code)
                     handle.write(url+i['href']+'\n')
                 except URLError as e:
                     print(url+i['href'] +': We failed to reach a server.')
                     print('Reason: ', e.reason)
                     handle.write(url + i['href'] + '\n')
                 else:
                     print(url+i['href'] + ': Website is working fine')
    handle.close




parceSite("http://138.68.49.60/TEST1/index.html")