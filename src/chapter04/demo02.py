# NumPy高级函数：获取矩阵主对角线上元素以及计算矩阵的迹
from numpy import *
# 矩阵的迹(迹数） 矩阵主对角线元素值的和

# diagonal：获取矩阵主对角线上的元素

a = array([2,3,5,1,7,4,8,4,3])
a.shape = (3,3)
print(a)

print(a.diagonal())

#  trace：获取矩阵的迹
print(a.trace())
