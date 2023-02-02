from pylab import *
from pandas import *
from numpy import *

# [0, 10000] [10000, 20000] [20000, 30000] [30000, 40000] [40000, 50000]
# [50000 70000] [70000 100000] [100000 150000] [150000 200000] [200000 250000]
# [250000 300000] [300000 350000] [350000 400000]

def merge(x):
    if x < 10000:
        return 5000
    elif x < 20000:
        return 15000
    elif x < 30000:
        return 25000
    elif x < 40000:
        return 35000
    elif x < 50000:
        return 45000
    elif x < 70000:
        return 60000
    elif x < 100000:
        return 85000
    elif x < 150000:
        return 125000
    elif x < 200000:
        return 175000
    elif x < 250000:
        return 225000
    elif x < 300000:
        return 275000
    elif x < 350000:
        return 325000
    else:
        return 375000

df = read_csv('price.csv')
df = DataFrame(df.values.T, index = df.columns, columns = df.index)
df = df.fillna('')

dfdict = df.to_dict()

for i in range(26):
    for j in range(2102):
        j += 1
        if type(dfdict[i][str(j)]) == str:
            continue
        dfdict[i][str(j)] = merge(dfdict[i][str(j)])

df1 = DataFrame.from_dict(dfdict)
df2 = DataFrame(df1.values.T, index = df1.columns, columns = df1.index)

df1.to_csv('priceMerged1.csv')
df2.to_csv('priceMerged2.csv')

import pdb
pdb.set_trace()
pass
