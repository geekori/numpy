# NumPy常用函数：读写CSV文件
from numpy import *

# 通过逗号分隔的文本文件

# savetxt和loadtxt
a = arange(20).reshape(4,5)
print(a)
savetxt('a.txt', a, fmt='%d', delimiter=',')

b = loadtxt('a.txt', dtype=int, delimiter=',', usecols=(1,3,4))
print(b)

x = loadtxt('x.txt', delimiter=',',usecols=(1,2,4))
print(x)
x,y,z = loadtxt('x.txt', delimiter=',',usecols=(1,2,4),unpack=True)
print(x,y,z)
