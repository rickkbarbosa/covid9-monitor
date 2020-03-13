#!/usr/bin/env python
#===============================================================================
# IDENTIFICATION DIVISION
#        ID SVN:   $Id$
#          FILE:  covid9_status.py
#         USAGE:  $0
#   DESCRIPTION:  Get Worldometers Coronavirus / Covid9 affected contry list
#  REQUIREMENTS:  pandas (pip install pandas)
#                 lxml (pip install lxml)
#          BUGS:  ---
#         NOTES:  ---
#          TODO:  ---
#        AUTHOR:  Ricardo Barbosa, rickkbarbosa@live.com
#       COMPANY:  ---
#       VERSION:  1.0
#       CREATED:  2020-Mar-10 08:57 BRT
#      REVISION:  ---
#===============================================================================

import pandas as pd
import json
import requests

url = 'https://www.worldometers.info/coronavirus/#countries'

df = pd.read_html(requests.get(url,headers={'User-agent': 'Mozilla/5.0'}).text)[0]
df = df['Country,Other']

country_list = list()
for i in range(0, len(df)):
    country_list.append({"{#COUNTRY_NAME}": df[i]})

print json.dumps({"data": country_list}, indent=4)
