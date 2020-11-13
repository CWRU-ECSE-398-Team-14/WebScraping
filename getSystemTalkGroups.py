# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 17:40:54 2020

@author: Bacon
"""

#edit so that it adds " before and after, as well as a , after
#one script for county ID to list all system IDs, found in <table class="rrtable content">
    #as (for example) <a href="/apps/db/?sid=7127">
    #Commonwealth Of Massachusetts Interoperable Radio System (CoMIRS)</a>
#one script for system ID to spit out the csv-style list of talkgroups
#str(number)
import requests
import pandas
from bs4 import BeautifulSoup
import sys
import json
from pandas import DataFrame as df 
sid = sys.argv[1]
#sid = "7337"
URL = 'https://www.radioreference.com/apps/db/?sid=' + sid + "&opt=all_tg#tgs"
#URL = 'https://www.radioreference.com/apps/db/?sid=7337&opt=all_tg#tgs'

page = requests.get(URL)
soup = BeautifulSoup(page.text, "html.parser")
freqTable = soup.find('table', attrs ={'class':'rrtable w1p'})
#tbody = freqTable.find('tbody')
trs = freqTable.find_all('tr')

thr = trs[0].find_all('th')
col_hddr = ""
for th in thr:
    col_hddr = col_hddr + " " + th.text + ", "
print(col_hddr[:-2])

row = ""
for tr in trs:
      tds = tr.find_all('td')
      for td in tds:
          row = row + " " + td.text + ", "
          #print(td.text)
      if len(tds) > 0:
          print(row[:-2])                         #UNCOMMENT THIS LINE to get talkgroups
      row = "" 
      
          
# with open('output.txt', 'w') as f:
#     for tr in soup.find_all('tr')[2:]:
#         tds = tr.find_all('td')
#         f.write("Nome: %s, Cognome: %s, Email: %s\n" % \
#               (tds[0].text, tds[1].text, tds[2].text))
          