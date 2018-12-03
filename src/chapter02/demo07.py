# NumPy数组：组合数组(深度组合）
from numpy import *

a = arange(12).reshape(2,6)
b = a * 2
c = a * 3
d = a * 4
print(a)
print(b)
print(c)
print(d)
e = dstack((a,b,c,d))
print(e)
print(e.shape)
print(a[0][0])  # 0
print(b[0][0])  # 0
print(c[0][0])  # 0
print(d[0][0])  # 0

print(e[0][0])
print(e[0][1])
print(e[1][1])
