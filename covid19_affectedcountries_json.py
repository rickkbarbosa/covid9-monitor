#!/usr/bin/env python
#===============================================================================
# IDENTIFICATION DIVISION
#        ID SVN:   $Id$
#          FILE:  covid9_affectedcountries_json.py
#         USAGE:  $0
#   DESCRIPTION:  Get Worldometers Coronavirus / Covid9 affected contry list
#  REQUIREMENTS:  pandas (pip install pandas)
#                 lxml (pip install lxml)
#				  geopy (pip install geopy)
#          BUGS:  ---
#         NOTES:  ---
#          TODO:  ---
#        AUTHOR:  Ricardo Barbosa, rickkbarbosa@live.com
#       COMPANY:  ---
#       VERSION:  1.0
#       CREATED:  2020-Mar-12 10:26 BRT
#      REVISION:  ---
#===============================================================================

import sys
import os
import json
import pandas as pd
from geopy.geocoders import Nominatim
import requests

reload(sys)
sys.setdefaultencoding('utf8')

here = os.path.dirname(os.path.abspath(__file__))
url = 'https://www.worldometers.info/coronavirus/#countries'
header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}
locator = Nominatim(user_agent="myGeocoder")

r = requests.get(url, headers=header)
df_countries = pd.read_html(r.text)[0]

#Online is a bad option
#df_iban = pd.read_html("https://www.iban.com/country-codes")[0]
#df_iban.to_csv("iban.csv")
df_iban = pd.read_csv("{}/{}".format(here, "iban.csv"))

result = pd.merge(df_countries,df_iban,left_on='Country,Other',right_on='Country',how='inner')

country_list = list()
for index, row in result.iterrows():

    location = locator.geocode("{}".format(row['Country,Other']))

    country_list.append({"key": row['Alpha-3 code'],
          "name": row['Country,Other'],
          "latitude": location.latitude,
          "longitude": location.longitude })


data = json.dumps({"data": country_list}, indent=4)

json_output = "/usr/share/zabbix/covid19_countries.json"
f = open(json_output,"w+")
f.write(data)
f.close()
