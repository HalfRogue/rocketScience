from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
from datetime import date
import requests

html = urlopen('https://www.cbr.ru/currency_base/daily/').read()
bs = BeautifulSoup(html, 'html.parser')
table = bs.find('table', {'class': 'data'})
rows = table.findAll(lambda tag: tag.name == 'tr')

data = []
for row in rows:
    cols = row.findAll('td')
    cols = [elem.text.strip() for elem in cols]
    data.append([elem for elem in cols if elem])
data = list(filter(None, data))
# print(data)

df = pd.DataFrame(np.array(data), columns=['dig_code', 'char_code', 'amount', 'name', 'value'])
usd = df.loc[df['char_code'] == 'USD', 'value'].values[0]
eur = df.loc[df['char_code'] == 'EUR', 'value'].values[0]
cny = df.loc[df['char_code'] == 'CNY', 'value'].values[0]
today = date.today()
# print(f'Курсы валют на {today}:\n USD = {usd}\n EUR = {eur}\n CNY = {cny}')

tkn = '5667558097:AAFaM0rvk7a7Z-sxLNfGvGGQVfbWTnHdSSI'
cht_id = '460823505'
msg = f'Курсы валют на {today}:\n USD = {usd}\n EUR = {eur}\n CNY = {cny}'
url = f'https://api.telegram.org/bot{tkn}/sendMessage?chat_id={cht_id}&text={msg}'
print(requests.get(url).json())