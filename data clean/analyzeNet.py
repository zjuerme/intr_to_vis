from math import *
from pylab import *
from pandas import read_csv
from pandas import DataFrame
from numpy import *
import tensorflow as tf
from tensorflow.keras import models, layers
from tensorflow.keras.constraints import max_norm

tmp = read_csv('processed.csv', encoding = 'gbk')

degree = list(tmp['degree'])
abv = list(tmp['abv'])
sweet = list(tmp['sweet'])
acidity = list(tmp['acidity'])
body = list(tmp['body'])
tannin = list(tmp['tannin'])
year = list(tmp['year'])
price = list(tmp['price'])

alllist = array([degree, abv, sweet, acidity, body, tannin, year]).T
alllabel = log(array(price))

i = 0
while i < alllist.shape[0]:
	if alllabel[i] > 150000:
		alllabel = delete(alllabel, i, axis = 0)
		alllist = delete(alllist, i, axis = 0)
	else:
		i += 1

trainlist = alllist[0:5000]
trainlabel = alllabel[0:5000]
testlist = alllist[5000:6616]
testlabel = alllabel[5000:6616]

trainlist = trainlist[:, :, newaxis]
testlist = testlist[:, :, newaxis]

import pdb
pdb.set_trace()

model = models.Sequential()
model.add(layers.Flatten(input_shape = (7, 1)))
model.add(layers.Dense(256, activation = 'relu'))
model.add(layers.Dense(128, activation = 'relu'))
model.add(layers.Dense(64, activation = 'relu'))
model.add(layers.Dense(1))

model.compile(optimizer='adam',
              loss=tf.keras.losses.MeanSquaredError(),
              # loss = tf.keras.losses.MeanSquaredError(), 
              metrics=['accuracy'])
history = model.fit(trainlist, trainlabel, epochs = 3000, batch_size = 3000)
print(model.evaluate(testlist, testlabel))

tmp = model.predict(trainlist).T[0]
plot(alllabel[0:5000], '*')
plot(tmp, '*')
show()

import pdb
pdb.set_trace()
pass
