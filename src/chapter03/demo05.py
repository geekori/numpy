# NumPy常用函数：时间加权平均价格
from numpy import *

# TWAP（Time-Weighted Average Price）

price, weights=loadtxt('data.csv', delimiter=',', usecols=(6,7),unpack=True)
vwap = average(price, weights = weights)
m = mean(price)
t = arange(len(price))
twap = average(price, weights = t)
print('vwap','=', vwap)
print('mean', '=', m)
print('twap', '=', twap)
