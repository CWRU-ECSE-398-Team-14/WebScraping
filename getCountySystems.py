# -*- coding: utf-8 -*-
"""
Spyder Editor 
This is a temporary script file.
"""
import requests
#import pandas
from bs4 import BeautifulSoup
import sys
#import json
#from pandas import DataFrame as df 

ctid = sys.argv[1]

URL = "https://www.radioreference.com/apps/db/?ctid=" + ctid
pageInitial = requests.get(URL)
soup = BeautifulSoup(pageInitial.text, "html.parser")


finalSID_set = set()
cid = ""
sidTemp = "sid="
p25table = soup.find_all('table', attrs ={'class':'rrtable content'}) #loop through this
print("System ID, System Name") # adam needs this for his code to work
for table in p25table:
    aTag = table.find_all('a')
    for a in aTag:
        checkp25 = 0
        tempString = a.get('href')
        tempIndex = tempString.find(sidTemp)
        tempName = str(a)
        tempName2begin = tempName.find(">")   
        tempName2end = tempName.find("</a>")
        finalSID = tempString[tempIndex + 4:] + ", "
        tempSystemInfo = table.text
        systemInfoStringBeginIndex = a.find("</b>")
        systemInfoStringEndIndex = a.find("</td>") 
        systemInfoString = tempSystemInfo[systemInfoStringBeginIndex:systemInfoStringEndIndex]   #these indexes don't always provide the correct info for checking if P25
        if "Project 25" in systemInfoString:                                                    #if two systems in same table and first one is p25, it always shows that the 2nd is as well
            checkp25 =1
    #if statement here checking if SID known
        if finalSID not in finalSID_set and checkp25 == 1:
            finalSID_set.add(finalSID)
            print(finalSID, end='')
            finalSystemName = tempName[tempName2begin+1:tempName2end]
            print(finalSystemName.strip())# + ", ")
            checkp25 =0

