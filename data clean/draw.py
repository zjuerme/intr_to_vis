from pylab import *
from numpy import *
from pandas import read_csv

data = read_csv('processed.csv', encoding = 'gbk')
lable='abv'
for lable in ['abv','degree','sweet','acidity','body','tannin','year']:
    x = array(list(data[lable]))
    y = array(list(data['price']))

    plot(x, y, '*')
    ylabel('Price')
    xlabel(lable)
    title('The correlation between '+lable+' and Price')
    show()