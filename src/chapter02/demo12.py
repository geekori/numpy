# NumPy数组：数组转换
from numpy import *

# tolist   astype

a = array([1,2,3,4,5,"a"])
print(a)
print(a.tolist())
b = a.reshape(2,3)
print(b)
print(b.tolist())

print(a.astype(int))
