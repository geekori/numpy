# NumPy常用函数：计算中位数和方差
from numpy import *

# 1，2，3，4，5,6

a = array([4,5,2,3,1])
print(median(a))

price =loadtxt('data.csv', delimiter=',', usecols=(6,),unpack=True)
print(price)
print(median(price))

sorted = msort(price)
print(sorted)
n = len(sorted)
print(n)
#print('middle', '=', sorted[(n - 1)//2])
# 取索引为14和15的两个值取平均数
print('middle', '=', (sorted[n // 2] + sorted[(n - 1)//2]) / 2)


#  方差：假设数组元素的算数平均数是a，元素个数是n，x1、x2、...、xn
#  ((x1 - a)^2 + (x2 - a)^2 + ... + (xn - a)^ 2) / n
# 方差：var
print('方差：',var(price))