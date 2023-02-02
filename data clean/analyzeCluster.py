from math import *
from pylab import *
from pandas import read_csv
from pandas import DataFrame
from numpy import *
from sklearn.cluster import KMeans

def normalization(data):
	dataMin = data.min(axis = 0)
	dataMax = data.max(axis = 0)
	return (dataMin, dataMax, (data - dataMin) / (dataMax - dataMin + 1))

tmp = read_csv('processed.csv', encoding = 'gbk')

alllist = array(tmp[['type', 'abv', 'degree', 'sweet', 'acidity', 'body', 'tannin', 'price', 'year']])
RedList = alllist[alllist[:, 0] == 'Red'][:, 1:9]				# 5340
WhiteList = alllist[alllist[:, 0] == 'White'][:, 1:9]			# 2023
RoseList = alllist[alllist[:, 0] == 'Rose'][:, 1:9]				# 123
FortifiedList = alllist[alllist[:, 0] == 'Fortified'][:, 1:9]	# 95
SparklingList = alllist[alllist[:, 0] == 'Sparkling'][:, 1:9]	# 664
EtcList = alllist[alllist[:, 0] == 'Etc'][:, 1:9]				# 29
HardList = alllist[alllist[:, 0] == 'Hard'][:, 1:9]				# 45

(RedMin, RedMax, RedList) = normalization(RedList)
(WhiteMin, WhiteMax, WhiteList) = normalization(WhiteList)
(RoseMin, RoseMax, RoseList) = normalization(RoseList)
(FortifiedMin, FortifiedMax, FortifiedList) = normalization(FortifiedList)
(SparklingMin, SparklingMax, SparklingList) = normalization(SparklingList)
(EtcMin, EtcMax, EtcList) = normalization(EtcList)
(HardMin, HardMax, HardList) = normalization(HardList)

clusterNum = [12, 12, 12, 12, 12, 12, 12]

redCluster = KMeans(n_clusters = clusterNum[0])
redCluster.fit(RedList)
redCenters = redCluster.cluster_centers_ * (RedMax - RedMin + 1) + RedMin

whiteCluster = KMeans(n_clusters = clusterNum[1])
whiteCluster.fit(WhiteList)
whiteCenters = whiteCluster.cluster_centers_ * (WhiteMax - WhiteMin + 1) + WhiteMin

roseCluster = KMeans(n_clusters = clusterNum[2])
roseCluster.fit(RoseList)
roseCenters = roseCluster.cluster_centers_ * (RoseMax - RoseMin + 1) + RoseMin

fortifiedCluster = KMeans(n_clusters = clusterNum[3])
fortifiedCluster.fit(FortifiedList)
fortifiedCenters = fortifiedCluster.cluster_centers_ * (FortifiedMax - FortifiedMin + 1) + FortifiedMin

sparklingCluster = KMeans(n_clusters = clusterNum[4])
sparklingCluster.fit(SparklingList)
sparklingCenters = sparklingCluster.cluster_centers_ * (SparklingMax - SparklingMin + 1) + SparklingMin

etcCluster = KMeans(n_clusters = clusterNum[5])
etcCluster.fit(EtcList)
etcCenters = etcCluster.cluster_centers_ * (EtcMax - EtcMin + 1) + EtcMin

hardCluster = KMeans(n_clusters = clusterNum[6])
hardCluster.fit(HardList)
hardCenters = hardCluster.cluster_centers_ * (HardMax - HardMin + 1) + HardMin

wineName = ['Red', 'White', 'Rose', 'Fortified', 'Sparkling', 'Etc', 'Hard']
allCenters = concatenate((redCenters, whiteCenters, roseCenters, fortifiedCenters, sparklingCenters, etcCenters, hardCenters), axis = 0)

tmpd = {}
tmpcount = 0
for i in range(len(wineName)):
	for j in range(clusterNum[i]):
		tmpd[wineName[i] + str(j)] = list(allCenters[tmpcount])
		tmpcount += 1
df = DataFrame.from_dict(tmpd)
df = DataFrame(df.values.T, index = df.columns, columns = ['abv', 'degree', 'sweet', 'acidity', 'body', 'tannin', 'price', 'year'])
df.to_csv('wineCluster.csv')

typeList = alllist[:, 0]
labelList = []
redId = 0
whiteId = 0
roseId = 0
fortifiedId = 0
sparklingId = 0
etcId = 0
hardId = 0

for i in range(len(typeList)):
	if typeList[i] == 'Red':
		labelList.append('Red' + str(redCluster.labels_[redId]))
		redId += 1
	elif typeList[i] == 'White':
		labelList.append('White' + str(whiteCluster.labels_[whiteId]))
		whiteId += 1
	elif typeList[i] == 'Rose':
		labelList.append('Rose' + str(roseCluster.labels_[roseId]))
		roseId += 1
	elif typeList[i] == 'Fortified':
		labelList.append('Fortified' + str(fortifiedCluster.labels_[fortifiedId]))
		fortifiedId += 1
	elif typeList[i] == 'Sparkling':
		labelList.append('Sparkling' + str(sparklingCluster.labels_[sparklingId]))
		sparklingId += 1
	elif typeList[i] == 'Etc':
		labelList.append('Etc' + str(etcCluster.labels_[etcId]))
		etcId += 1
	elif typeList[i] == 'Hard':
		labelList.append('Hard' + str(hardCluster.labels_[hardId]))
		hardId += 1

labelList = array(labelList)

tmp.insert(29, 'Label', 1)
tmp['Label'] = labelList
tmp.to_csv('processedWithLabel.csv')

import pdb
pdb.set_trace()
pass
