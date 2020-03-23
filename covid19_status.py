#!/usr/bin/env python
#===============================================================================
# IDENTIFICATION DIVISION
#        ID SVN:   $Id$
#          FILE:  covid9_status.py
#         USAGE:  $0
#   DESCRIPTION:  Get Worldometers Coronavirus / Covid9 data and print to JSON
#  REQUIREMENTS:  pandas (pip install pandas)
#                 lxml (pip install lxml)
#                 beautifulsoup4 (pip install beautifulsoup4)
#          BUGS:  ---
#         NOTES:  ---
#          TODO:  ---
#        AUTHOR:  Ricardo Barbosa, rickkbarbosa@live.com
#       COMPANY:  ---
#       VERSION:  1.0
#       CREATED:  2020-Mar-10 21:47 BRT
#      REVISION:  2020-Mar-20 09:33 BRT
#===============================================================================

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.worldometers.info/coronavirus/#countries'
header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}

r = requests.get(url, headers=header)

# fix HTML multiple tbody
soup = BeautifulSoup(r.text, "html.parser")
for body in soup("tbody"):
    body.unwrap()

df = pd.read_html(str(soup), index_col=0, thousands=r',', flavor="bs4")[0]
df = df.replace(regex=[r'\+', r'\,'], value='')

df = df.fillna('0')
df = df.to_json(orient='index')

print(df)
