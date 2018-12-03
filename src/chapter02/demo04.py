# NumPy数组：改变数组的维度
from numpy import *
b = arange(24).reshape(2,3,4)
print(b)
# reshape、resize、ravel、flatten、transpose、元组
# 方法1：使用ravel
b1 = b.ravel()
print(b1)

# 方法2：使用flatten
b2 = b.flatten()
print(b2)
#  ravel返回数组的一个视图，修改视图的值，会影响到原来的数组
#  flatten户请求新的内存来保存结果，修改返回结果并不会影响原来的数组
b1[0] = 100
print(b)
b2[1] = 200
print(b)

# 方法3：使用元组设置数组维度

b.shape = (6,4)
print(b)

# 方法4：transpose
b3 = b.transpose()
print(b3)
b3[0][0] = 10000
print(b)

# 方法5：resize方法
# resize和reshape
b.resize((2,12))
print(b)
