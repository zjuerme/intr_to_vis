from math import *
from pylab import *
from pandas import read_csv
from pandas import DataFrame
from numpy import *

tmp = read_csv('processed.csv', encoding = 'gbk')

degree = list(tmp['degree'])
abv = list(tmp['abv'])
sweet = list(tmp['sweet'])
acidity = list(tmp['acidity'])
body = list(tmp['body'])
tannin = list(tmp['tannin'])
year = list(tmp['year'])
price = list(tmp['price'])

dataMat = stack((degree, abv, sweet, acidity, body, tannin, year, price), axis = 0)
covMat = cov(dataMat)
print(covMat)

import pdb
pdb.set_trace()
pass
