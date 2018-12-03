# NumPy常用函数：计算阶乘
from numpy import *

#  prod  cumprod

# 10的阶乘
a = arange(1,11)
print('a',a)
print('10！','=',a.prod())

print('1到10的阶乘',a.cumprod())








