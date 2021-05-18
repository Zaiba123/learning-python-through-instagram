import matplotlib.pyplot as p
import requests 
import pandas as pd
from pandas import DataFrame
from IPython.core.display import HTML

r = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false')  #to timeout on request 
r_data = r.json()

crypto_name_list = []
crypto_price_list = []

for i in range(4):
    crypto_name_list.append((r_data[i]["name"]))

for i in range(4):
    crypto_price_list.append((r_data[i]["current_price"]))


p.bar(crypto_name_list,crypto_price_list)
# p.legend(title = "Crypto Currencies")

p.show()

# print(crypto_name_list)