# NumPy常用函数：寻找最大值和最小值,以及计算数组的取值范围
from numpy import *

h,l=loadtxt('data.csv', delimiter=',', usecols=(4,5),unpack=True)
print(h)
print(l)

print('highest', '=', max(h))
print('lowest','=', min(l))

print('范围','=',max(h) - min(h))

print('范围','=',ptp(h))

