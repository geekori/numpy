# NumPy数组：分割数组
from numpy import *
# 水平分割、垂直分割、深度分割

# 水平分割

a = arange(9).reshape(3,3)
print(a)

b = hsplit(a,3)
print(b[0])
print(b[2])

# 垂直分割
print("---------")
c = vsplit(a,3)
print(c)
print(c[0])
print(c[2])

# 深度分割

a = arange(27).reshape(3,3,3)
print(a)

b = dsplit(a,3)
print(b)
