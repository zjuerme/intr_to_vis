from pylab import *
import numpy as np
import pandas as pd
from numpy import *
from pandas import read_csv
data = read_csv('processed.csv', encoding = 'gbk')
a = array(list(data['abv']))
b = array(list(data['degree']))
c = array(list(data['sweet']))
d = array(list(data['acidity']))
e = array(list(data['body']))
f= array(list(data['tannin']))
g= array(list(data['year']))
p = array(list(data['price']))

array=[a,b,c,d,e,f,g,p]

for i in range(8):
    for j in range(8):
        pea = np.corrcoef(array[i], array[j])
        print(pea[0][1])
    print('\n')
