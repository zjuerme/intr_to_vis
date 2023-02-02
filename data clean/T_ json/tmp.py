import pandas as pd
import math

data=pd.read_csv("price.csv")

header=None#加上此句可以恢复表头
thislist=data.values.tolist()

for i in range(len(thislist)):
  for j in range(len(thislist[i])):
    if math.isnan(thislist[i][j]):
      break
  thislist[i] = thislist[i][0:j]

thislist[1]= list(map(int, thislist[1]))
for i in range(len(thislist)):
  thislist[i]=list(map(int,thislist[i]))
print(thislist[25])