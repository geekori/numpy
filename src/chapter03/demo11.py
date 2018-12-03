# NumPy常用函数：数组的修剪和压缩
from numpy import *

# clip   compress

# 数组的修剪：将所有比给定最大值还大的数组值都设为给定的最大值，
# 将所有比给定最小值还小的数组值都设为给定的最小值

a = arange(10)
print('a', a)
print('clipped', a.clip(3,5))

print('Compressed', a.compress(a > 4))


