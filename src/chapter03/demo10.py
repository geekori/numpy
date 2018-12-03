# NumPy常用函数：用线性模型进行预测（最小二乘法、梯度）
from numpy import *

#  线性模型：  直线方程 f(x)  f(x1,x2)   预测就是根据x求对应的y

#  问题变成了求直线方程
'''
提供一组离散点，通过数学公式，计算出总体上最接近这些离散点的直线
通过直线就会得到一个直线方程

(1,6)
(2,5)
(3,7)
(4,10)
(5,10.5)
y = b1 * x + b2

6 = b1 * 1 + b2
5 = b1 * 2 + b2
7 = b1 * 3 + b2
10 = b1 * 4 + b2

f(b1,b2) = (6 - (b1 * 1 + b2)) ^ 2 + (5 - (b1 * 2 + b2)) ^ 2 + 
           (7 - (b1 * 3 + b2)) ^ 2 + (10 - (b1 * 2 + b2)) ^ 2

min(f(b1,b2))  求函数的最小值就是最小二乘法

f(x)
d(f(x))/d(x) = 0

二元函数需要求偏导
d(f(b1,b2))/d(b1) = 0
d(f(b1,b2))/d(b2) = 0

d(f(b1,b2))/d(b1) = 20b1 + 8b2 - 56 = 0
d(f(b1,b2))/d(b2) = 60b1 + 20b2 - 154 = 0
20b1 + 8b2 - 56 = 0
60b1 + 20b2 - 154 = 0

b1 = 1.4
b2 = 3.5

y = b1 * x + b2

y = 1.4 * x + 3.5  (直线方程）

y = 1.4 * 5 + 3.5  = 10.5 

lstsq: 返回线性矩阵方程的最小二乘法的解
dot:用来计算两个向量的乘积
(1,6)
(2,5)
(3,7)
(4,10)
'''
x = array([1,2,3,4])
y = array([6,5,7,10])
a = vstack([x, ones(len(x))]).T
print(a)
b1,b2= linalg.lstsq(a, y)[0]
print(b1,b2)

from matplotlib.pyplot import *
plot(x,y,'o', label='Point', markersize=15)
plot(x, b1 * x + b2,'b',label='Fitter Line') # 拟合直线
legend()
show()

a = array([3,4])
b = array([2,3])

print(dot(a,b))
