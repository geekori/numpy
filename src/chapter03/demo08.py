# NumPy常用函数：计算股票收益率和波动率
from numpy import *

# 简单收益率：相邻两个价格之间的变化率
# 20  30  50  45     (30 - 20)/20, (50 - 30) / 30, (45 - 50) / 45
# 对数收益率: 所有价格取对数后两两之间的差值
# (log(30) - log(20)) = log(30/20)，log(50)-log(30)，log(45)-log(50)
# log(a) - log(b) = log(a/b)

# diff、std、where、log、sqrt
# diff：返回由相邻数组元素的差值组成的数组，10、20、-5
# std：计算标准差：sqrt(((x1 - a)^2 + (x2 - a)^2 + ... + (xn - a)^ 2) / n)
# 标准差可以反映一个数据集的离散程度
# where：可以根据设置的条件过滤数组中的值（索引）

# 计算简单收益率
a = array([4,7,10,4])
print(diff(a))

c = loadtxt('data.csv', delimiter=',', usecols=(6,),unpack=True)
print(c)

returns = diff(c) / c[:-1]
print(returns)
print("标准差：",std(returns))

# 计算对数收益率
logreturns = diff(log(c))
print(logreturns)

# 过滤正的收益率
print('简单收益率（正）',where(returns > 0))
print('对数收益率（正）', where(logreturns > 0))


# 股票波动率：是对价格变动的一种衡量。
# 年股票波动率：对数收益率的标准差除以对数收益率的平均值，然后再除以252个工作日的倒数的平方根
annualVolatility = std(logreturns)/mean(logreturns)
annualVolatility = annualVolatility / sqrt(1/252)
print("年波动率", annualVolatility)

print("月波动率", annualVolatility * sqrt(1/12))



