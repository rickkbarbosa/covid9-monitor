#!/usr/bin/env python
#===============================================================================
# IDENTIFICATION DIVISION
#        ID SVN:   $Id$
#          FILE:  covid9_status.py
#         USAGE:  $0
#   DESCRIPTION:  Get Worldometers Coronavirus / Covid9 data and print to JSON
#  REQUIREMENTS:  pandas (pip install pandas)
#                 lxml (pip install lxml)
#          BUGS:  ---
#         NOTES:  ---
#          TODO:  ---
#        AUTHOR:  Ricardo Barbosa, rickkbarbosa@live.com
#       COMPANY:  ---
#       VERSION:  1.0
#       CREATED:  2020-Mar-10 21:47 BRT
#      REVISION:  ---
#===============================================================================

import pandas as pd
import requests

url = 'https://www.worldometers.info/coronavirus/#countries'

df = pd.read_html(requests.get(url,headers={'User-agent': 'Mozilla/5.0'}).text, index_col=0)[0]
df = pd.read_html(url, index_col=0)[0]
df = df.fillna('0')
df = df.to_json(orient='index')

print(df)
