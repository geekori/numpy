# NumPy数组：组合数组(列组合）
from numpy import *
a = arange(5)
b = a * 2
c = a * 3
print(a)
print(b)
print(c)
d = column_stack((a,b,c))
print(d)
print(d.shape)

a = arange(12).reshape(3,4)
b = a * 2
c = a * 3
d = column_stack((a,b,c))
print("-----------")
print(a)
print(b)
print(c)
print(d)

