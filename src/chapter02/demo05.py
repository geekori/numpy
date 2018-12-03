# NumPy数组：组合数组(水平组合）
from numpy import *

# A
# B 
# A B  A和B行数相同，列数可以不同
# hstack可以水平组合任意多个数组，但这些数组必须行数相同，否则会抛出异常
a = arange(9).reshape(3,3)
b = a * 3
print(a)
print(b)
c = a * 5
d = arange(12).reshape(3,4)
print(hstack((a,b)))
print(hstack((a,b,c)))
print(hstack((a,d)))
e = arange(12).reshape(4,3)
print(hstack((a,e)))