# NumPy常用函数：读写文本文件
from numpy import *
'''
1. 读写文件的函数
2. 与数组先关的一些函数
3. 一些简单的数学和统计分析函数

'''
a = arange(20)
print(a)

savetxt("a.txt", a,fmt='%d')
savetxt("b.txt", a,fmt='%.2f')

aa = loadtxt("a.txt",dtype='int')
bb = loadtxt("b.txt", dtype='float')
print(aa)
print(bb)

x = arange(16).reshape(4,4)
print(x)
savetxt("x.txt",x,fmt='%d')

y = loadtxt("x.txt",dtype='int')
print(y)
