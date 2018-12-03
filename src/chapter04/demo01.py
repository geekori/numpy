# NumPy高级函数：计算协方差矩阵
from numpy import *

a = array([1,3,4,5])
b = array([2,6,2,2])
x = vstack((a,b))
print(x)
print(cov(x))

#  cov函数会将正常的结果缩小到原来的1/3