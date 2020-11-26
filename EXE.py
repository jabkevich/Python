import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import URLError, HTTPError


def parserSite(url):
    r = requests.get(url)
    page = BeautifulSoup(r.text, 'html.parser')
    handle = open('test.txt', 'w')
    for i in page.findAll('a', href=True):
        if i['href'][0:4] == "http":
            try:
                urlopen(i['href'])
            except HTTPError as e:
                print(i['href'] + ': The server couldn\'t fulfill the request.')
                print('Error code: ', e.code)
                handle.write(i['href'] + '\n')
            except URLError as e:
                print(i['href'] + ': We failed to reach a server.')
                print('Reason: ', e.reason)
                handle.write(url + i['href'] + '\n')
            else:
                print(i['href'] + ': Website is working fine')
        elif i['href'][0:4] == "tel:":
            print(i['href'] + ':  - это телефон')
        else:
            try:
                hr = url + '/' + i['href']
                urlopen(hr.replace(' ', ''))
            except HTTPError as e:
                print(url + i['href'] + ': The server couldn\'t fulfill the request.')  # оно
                print('Error code: ', e.code)
                handle.write(url + i['href'] + '\n')
            except URLError as e:
                print(url + i['href'] + ': We failed to reach a server.')
                print('Reason: ', e.reason)
                handle.write(url + i['href'] + '\n')
            else:
                print(url + i['href'] + ': Website is working fine')
    handle.close()


parserSite("https://itmo.ru/ru/")
