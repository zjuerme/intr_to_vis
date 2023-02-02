from math import *
from pandas import read_csv
from pandas import DataFrame
from numpy import *

tmp = read_csv('cleansingWine.csv')

name = list(tmp['name'])
degree = list(tmp['degree'])
abv = list(tmp['abv'])
sweet = list(tmp['sweet'])
acidity = list(tmp['acidity'])
body = list(tmp['body'])
tannin = list(tmp['tannin'])
price = list(tmp['price'])
year = list(tmp['year'])
ml = list(tmp['ml'])
nation = list(tmp['nation'])
local1 = list(tmp['local1'])
local2 = list(tmp['local2'])
local3 = list(tmp['local3'])
local4 = list(tmp['local4'])
wineType = list(tmp['type'])
use =  list(tmp['use'])

var1 = list(tmp['varieties1'])
var2 = list(tmp['varieties2'])
var3 = list(tmp['varieties3'])
var4 = list(tmp['varieties4'])
var5 = list(tmp['varieties5'])
var6 = list(tmp['varieties6'])
var7 = list(tmp['varieties7'])
var8 = list(tmp['varieties8'])
var9 = list(tmp['varieties9'])
var10 = list(tmp['varieties10'])
var11 = list(tmp['varieties11'])
var12 = list(tmp['varieties12'])

# Delete the odd item
i = 0
while i < len(degree):
	if year[i] == 0:
		year[i] = 2021
	if type(degree[i]) != str or type(abv[i]) != str or type(sweet[i]) != str or \
		type(acidity[i]) != str or type(body[i]) != str or type(tannin[i]) != str or \
		isnan(price[i]) or price[i] == 0 or type(var1[i]) != str or isnan(ml[i]) or ml[i] == 0:
		del name[i]
		del degree[i]
		del abv[i]
		del sweet[i]
		del acidity[i]
		del body[i]
		del tannin[i]
		del price[i]
		del year[i]
		del ml[i]
		del nation[i]
		del local1[i]
		del local2[i]
		del local3[i]
		del local4[i]
		del wineType[i]
		del use[i]

		del var1[i]
		del var2[i]
		del var3[i]
		del var4[i]
		del var5[i]
		del var6[i]
		del var7[i]
		del var8[i]
		del var9[i]
		del var10[i]
		del var11[i]
		del var12[i]
	else:
		year[i] = 2021 - year[i]
		price[i] = price[i] * 750 / ml[i]
		i += 1

preAbv = []
preDeg = []
preSweet = []
preAcidity = []
preBody = []
preTannin = []

for i in range(len(abv)):
	if '~' in abv[i]:
		[tx, ty] = abv[i].split('~')
		tx = float(tx)
		ty = float(ty)
		preAbv.append((tx + ty) / 2)
	else:
		preAbv.append(float(abv[i]))

	if '~' in degree[i]:
		[tx, ty] = degree[i].split('~')
		tx = float(tx)
		ty = float(ty)
		preDeg.append((tx + ty) / 2)
	else:
		preDeg.append(float(degree[i]))

	preSweet.append(float(sweet[i][5]))
	preAcidity.append(float(acidity[i][7]))
	preBody.append(float(body[i][4]))
	preTannin.append(float(tannin[i][6]))

tmpVar = []
preVar1 = []
preVar2 = []
preVar3 = []
preVar4 = []
preVar5 = []
preVar6 = []
preVar7 = []
preVar8 = []
preVar9 = []
preVar10 = []
preVar11 = []
preVar12 = []
for i in range(len(var1)):
	if var1[i] not in tmpVar:
		tmpVar.append(var1[i])
	if type(var2[i]) == str and var2[i] not in tmpVar:
		tmpVar.append(var2[i])
	if type(var3[i]) == str and var3[i] not in tmpVar:
		tmpVar.append(var3[i])
	if type(var4[i]) == str and var4[i] not in tmpVar:
		tmpVar.append(var4[i])
	if type(var5[i]) == str and var5[i] not in tmpVar:
		tmpVar.append(var5[i])
	if type(var6[i]) == str and var6[i] not in tmpVar:
		tmpVar.append(var6[i])
	if type(var7[i]) == str and var7[i] not in tmpVar:
		tmpVar.append(var7[i])
	if type(var8[i]) == str and var8[i] not in tmpVar:
		tmpVar.append(var8[i])
	if type(var9[i]) == str and var9[i] not in tmpVar:
		tmpVar.append(var9[i])
	if type(var10[i]) == str and var10[i] not in tmpVar:
		tmpVar.append(var10[i])
	if type(var11[i]) == str and var11[i] not in tmpVar:
		tmpVar.append(var11[i])
	if type(var12[i]) == str and var12[i] not in tmpVar:
		tmpVar.append(var12[i])

	preVar1.append(tmpVar.index(var1[i]))
	if type(var2[i]) == str:
		preVar2.append(tmpVar.index(var2[i]))
	else:
		preVar2.append(-1)
	if type(var3[i]) == str:
		preVar3.append(tmpVar.index(var3[i]))
	else:
		preVar3.append(-1)
	if type(var4[i]) == str:
		preVar4.append(tmpVar.index(var4[i]))
	else:
		preVar4.append(-1)
	if type(var5[i]) == str:
		preVar5.append(tmpVar.index(var5[i]))
	else:
		preVar5.append(-1)
	if type(var6[i]) == str:
		preVar6.append(tmpVar.index(var6[i]))
	else:
		preVar6.append(-1)
	if type(var7[i]) == str:
		preVar7.append(tmpVar.index(var7[i]))
	else:
		preVar7.append(-1)
	if type(var8[i]) == str:
		preVar8.append(tmpVar.index(var8[i]))
	else:
		preVar8.append(-1)
	if type(var9[i]) == str:
		preVar9.append(tmpVar.index(var9[i]))
	else:
		preVar9.append(-1)
	if type(var10[i]) == str:
		preVar10.append(tmpVar.index(var10[i]))
	else:
		preVar10.append(-1)
	if type(var11[i]) == str:
		preVar11.append(tmpVar.index(var11[i]))
	else:
		preVar11.append(-1)
	if type(var12[i]) == str:
		preVar12.append(tmpVar.index(var12[i]))
	else:
		preVar12.append(-1)

import pdb
pdb.set_trace()

lst = []
for i in range(len(abv)):
	lst.append({'name': name[i], 'nation': nation[i], 'local1': local1[i], 'local2': local2[i], 'local3': local3[i], 'local4': local4[i], 'type': wineType[i], 'use': use[i], 'abv': preAbv[i], 'degree': preDeg[i], 'sweet': preSweet[i], 'acidity': preAcidity[i], 'body': preBody[i], 'tannin': preTannin[i], 'price': price[i], 'year': year[i], \
				'varieties1': preVar1[i], 'varieties2': preVar2[i], 'varieties3': preVar3[i], 'varieties4': preVar4[i], 'varieties5': preVar5[i], 'varieties6': preVar6[i], 'varieties7': preVar7[i], 'varieties8': preVar8[i], 'varieties9': preVar9[i], 'varieties10': preVar10[i], 'varieties11': preVar11[i], 'varieties12': preVar12[i]})

df = DataFrame(lst)
df.to_csv('processed.csv', columns = ['name', 'nation', 'local1', 'local2', 'local3', 'local4', 'type', 'use', 'abv', 'degree', 'sweet', 'acidity', 'body', 'tannin', 'price', 'year', 'varieties1', 'varieties2', 'varieties3', 'varieties4', 'varieties5', 'varieties6', 'varieties7', 'varieties8', 'varieties9', 'varieties10', 'varieties11', 'varieties12'], header = ['name', 'nation', 'local1', 'local2', 'local3', 'local4', 'type', 'use', 'abv', 'degree', 'sweet', 'acidity', 'body', 'tannin', 'price', 'year', 'varieties1', 'varieties2', 'varieties3', 'varieties4', 'varieties5', 'varieties6', 'varieties7', 'varieties8', 'varieties9', 'varieties10', 'varieties11', 'varieties12'], index_label = 'id')

import pdb
pdb.set_trace()

pass