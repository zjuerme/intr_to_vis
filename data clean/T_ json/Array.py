import pandas as pd
import numpy as np

path1 = "Etc1"
path2 = "Fortified1"
path3 = "Hard1"
path4 = "Red1"
path5 = "Rose1"
path6 = "Sparkling1"
path7 = "White1"
path8 = "../wineCountryNum"
path9 = "Cluster"
path10 = 'France'
path11 = 'price'
data=pd.read_csv(path11+".csv")

header=None#加上此句可以恢复表头
thislist=data.values.tolist()
thislist[1]= list(map(int, thislist[1]))
thislist.dropna(inplace=False)
#for i in thislist:
  # i=list(map(int, i))
print(thislist[1])