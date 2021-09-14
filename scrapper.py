# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:27:22 2021

@author: maela
"""

import requests
from bs4 import BeautifulSoup

url = 'http://example.python-scraping.com/'

response = requests.get(url)

# ok if code equals 200
if response.ok:
    links = []
    # print html code
    # print(response.text)
    
    # html code ca be parsed
    soup = BeautifulSoup(response.text, 'lxml')
    
    # get title from the web page
    title = soup.find('title')
    
    tds = soup.findAll('td')
    print(len(tds))
    
    
    #[print(str(td) + '\n\n') for td in tds]
    
    for td in tds:
        n = td.find('a')
        link = n['href']
        links.append(link)

        print('http://example.python-scraping.com/' + link)
else:
    print("error with get url")
    
