from math import *
from pylab import *
from pandas import read_csv
from pandas import DataFrame
from numpy import *

tmp = read_csv('processed.csv', encoding = 'gbk')

nation = list(tmp['nation'])
price = list(tmp['price'])

dictionaryPrice = {}

for i in range(len(nation)):
	if type(nation[i]) != str or type(price[i]) != float:
		continue

	if nation[i] not in dictionaryPrice:
		dictionaryPrice[nation[i]] = {'price': 0, 'count': 0, 'avg': 0};

	dictionaryPrice[nation[i]]['price'] += price[i]
	dictionaryPrice[nation[i]]['count'] += 1

for i in list(dictionaryPrice.keys()):
	dictionaryPrice[i]['avg'] = dictionaryPrice[i]['price'] / dictionaryPrice[i]['count']


df1 = DataFrame.from_dict(dictionaryPrice)
df1 = DataFrame(df1.values.T, index = df1.columns, columns = df1.index)
df1.to_csv('wineCountryAvgPrice.csv')

import pdb
pdb.set_trace()
pass
