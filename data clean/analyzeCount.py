from math import *
from pylab import *
from pandas import read_csv
from pandas import DataFrame
from numpy import *

tmp = read_csv('processed.csv', encoding = 'gbk')

nation = list(tmp['nation'])
wineType = list(tmp['type'])
use = list(tmp['use'])

dictionaryNum = {}
dictionaryUse = {}

for i in range(len(nation)):
	if type(nation[i]) != str or type(wineType[i]) != str or type(use[i]) != str:
		continue

	if nation[i] not in dictionaryNum:
		dictionaryNum[nation[i]] = {'Red': 0, 'White': 0, 'Rose': 0, 'Fortified': 0, 'Sparkling': 0, 'Etc': 0, 'Hard': 0}
	if nation[i] not in dictionaryUse:
		dictionaryUse[nation[i]] = {}

	if use[i] not in dictionaryUse[nation[i]]:
		dictionaryUse[nation[i]][use[i]] = 0
	# if wineType[i] not in dictionary[nation[i]]:
	# 	dictionary[nation[i]][wineType[i]] = 0

	dictionaryNum[nation[i]][wineType[i]] += 1
	dictionaryUse[nation[i]][use[i]] += 1
'''
lst = []
nationKeys = list(dictionaryNum.keys())
import pdb
pdb.set_trace()
for i in range(len(nationKeys)):
	lst.append({'nation': nationKeys[i], 'Red': dictionaryNum[nationKeys[i]]['Red'], 'White': dictionaryNum[nationKeys[i]]['White'], 'Rose': dictionaryNum[nationKeys[i]]['Rose'], 'Fortified': dictionaryNum[nationKeys[i]]['Fortified'], 'Sparkling': dictionaryNum[nationKeys[i]]['Sparkling'], 'Etc': dictionaryNum[nationKeys[i]]['Etc'], 'Hard': dictionaryNum[nationKeys[i]]['Hard'], 'Korean': dictionaryNum[nationKeys[i]]['Korean'], 'Sake/Rice': dictionaryNum[nationKeys[i]]['Sake/Rice']}) 

df = DataFrame(lst)
df.to_csv('wineCountryUsage.csv', columns = ['nation', 'Red', 'White', 'Rose', 'Fortified', 'Sparkling', 'Etc', 'Hard', 'Korean', 'Sake/Rice'], header = ['nation', 'Red', 'White', 'Rose', 'Fortified', 'Sparkling', 'Etc', 'Hard', 'Korean', 'Sake/Rice'], index_label = 'id')
'''

df1 = DataFrame.from_dict(dictionaryNum)
df1 = DataFrame(df1.values.T, index = df1.columns, columns = df1.index)
df1.to_csv('wineCountryNum.csv')

df2 = DataFrame.from_dict(dictionaryUse)
df2 = df2.fillna(0)
df2 = DataFrame(df2.values.T, index = df2.columns, columns = df2.index)
df2.to_csv('wineCountryUsage.csv')

import pdb
pdb.set_trace()
pass
