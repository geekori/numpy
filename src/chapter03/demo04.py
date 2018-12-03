# NumPy常用函数：算数平均值
from numpy import *
# mean
price, weights=loadtxt('data.csv', delimiter=',', usecols=(6,7),unpack=True)
vwap = average(price, weights = weights)
m = mean(price)
print('vwap','=', vwap)
print('mean', '=', m)

a = arange(100)  # (0 + 1 + 2 + ... + 99) / 100 
m = mean(a)
print(m)