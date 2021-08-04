#!/usr/bin/env python
#===============================================================================
# IDENTIFICATION DIVISION
#        ID SVN:   $Id$
#          FILE:  covid9_status.py
#         USAGE:  $0
#   DESCRIPTION:  Get Worldometers Coronavirus / Covid9 affected contry list
#  REQUIREMENTS:  pandas (pip install pandas)
#                 lxml (pip install lxml)
#                 beautifulsoup4 (pip install beautifulsoup4)
#          BUGS:  ---
#         NOTES:  ---
#          TODO:  ---
#        AUTHOR:  Ricardo Barbosa, rickkbarbosa@live.com
#       COMPANY:  ---
#       VERSION:  1.0
#       CREATED:  2020-Mar-10 08:57 BRT
#      REVISION:  2020-Mar-20 09:54 BRT
#===============================================================================

import sys
import os
import pandas as pd
import json
import re
import requests
from bs4 import BeautifulSoup

if(sys.version_info.major>=3):
    import importlib
    importlib.reload(sys)
else:
    reload(sys)
    sys.setdefaultencoding('utf8')

here = os.path.dirname(os.path.abspath(__file__))
url = 'https://www.worldometers.info/coronavirus/#countries'
header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}

r = requests.get(url, headers=header).text
r = re.sub(r'.*(<table id="main_table_countries_today".*?>.*?<\/table>).*', r'\1', r, flags=re.DOTALL)
r = re.sub(r'<tbody class="body_continents">.*?<\/tbody>', '', r, flags=re.DOTALL)
r = re.sub(r'<.*?>', lambda g: g.group(0).upper(), r)

# fix HTML multiple tbody
soup = BeautifulSoup(r, "html.parser")
for body in soup("tbody"):
    body.unwrap()

df_countries = pd.read_html(str(soup), flavor="bs4")[0]


df_iban = pd.read_csv("{}/{}".format(here, "iban.csv"))
result = pd.merge(df_countries,df_iban,left_on='Country,Other',right_on='Country',how='inner')

country_list = list()
for index, row in result.iterrows():
    country_list.append({"{#COUNTRY_NAME}": row['Country,Other'],
                        "{#COUNTRY_IBAN}": row['Alpha-3 code'] })

    data = json.dumps({"data": country_list}, indent=4)

print(data)
