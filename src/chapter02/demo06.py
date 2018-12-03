# NumPy数组：组合数组(垂直组合）
from numpy import *

# vstack
a = arange(12).reshape(3,4)
b = arange(16).reshape(4,4)
c = arange(20).reshape(5,4)
d = arange(20).reshape(4,5)
print(a)
print(b)
print(c)
print(vstack((a,b,c)))
