#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 23:22:19 2021

@author: matsushimataichi
"""

import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.yahoo.co.jp/'
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")
elems = soup.find_all(href=re.compile("https://news.yahoo.co.jp/pickup"))
#print(elems[0].contents[0].text)
#print(elems[0].attrs['href'])

with open('st.text', mode='w', encoding = 'utf-8') as fw:
    for elem in elems:
        print(elem.contents[0].text)
        print(elem.attrs['href'])
        fw.write(elem.contents[0].text + "\n")
        fw.write(elem.attrs['href'] + "\n")