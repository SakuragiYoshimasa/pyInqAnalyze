# coding: utf-8
import sys
import pandas as pd
import json
import requests
from apikey import apikey

book = 'Data/Inquiry.xlsx'
df_list = []
file = pd.ExcelFile(book, encoding='utf-8') # bookを読む
for sheet in file.sheet_names:
    df_list.append(file.parse(sheet))
df = df_list[0]

print(df)

for d in df['Description']:

    #sentence_in = "I got up early today."
    sentence_in = d
    print(sentence_in)

    url="https://translation.googleapis.com/language/translate/v2/"
    url += "?key=" + apikey
    url += "&q=" + sentence_in
    url += "&target=ja"
    rr=requests.get(url)
    transed=json.loads(rr.text)
    print(transed)
    result = transed["data"]["translations"][0]["translatedText"]
    print(result)
