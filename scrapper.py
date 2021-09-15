# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:27:22 2021

@author: maela
"""

import requests
from bs4 import BeautifulSoup

'''links = []
for i in range(26):
    
    
    url = 'http://example.python-scraping.com/places/default/index/' + str(i)
    
    response = requests.get(url)
    
    # ok if code equals 200
    if response.ok == False:
        print("error with get url")
    
        
    else:
        print("Page " + str(i))
        # print html code
        # print(response.text)
        
        # html code ca be parsed
        soup = BeautifulSoup(response.text, 'lxml')
        
        # get title from the web page
        title = soup.find('title')
        
        tds = soup.findAll('td')
        #print(len(tds))
        
        
        #[print(str(td) + '\n\n') for td in tds]
        
        for td in tds:
            n = td.find('a')
            link = n['href']
            links.append('http://example.python-scraping.com' +  link)
    
print(len(links))

#write in a txt file
with open('urls.txt', 'w') as file:
    for link in links:
        file.write(link + '\n')
       
'''
with open('urls.txt', 'r') as file:
    with open('pays.csv', 'w') as outfile:
        outfile.write('pays, population\n')
        for row in file:     
            
            url = row.strip()
            
            response = requests.get(url)
            
            if response.ok:
                soup = BeautifulSoup(response.text, 'lxml')
                country = soup.find('tr', {'id':'places_country_or_district__row'}).find('td', {'class':'w2p_fw'})
                
                population = soup.find('tr', {'id':'places_population__row'}).find('td', {'class':'w2p_fw'})
                outfile.write(country.text + ', ' + population.text.replace(',', '') + '\n')
                print('Pays : ' + str(country.text) + ' avec comme population : ' + str(population.text))
                    
                    
        
        
        
        
        
        
        
        
        