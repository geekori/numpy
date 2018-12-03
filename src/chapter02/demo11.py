# NumPy数组：数组的属性
from numpy import *
# shape  dtype
# shape：通过元组的形式返回数组每一维度元素的个数
# dtype：返回数组的元素类型

a = arange(16).reshape(2,8)
print(a)
print(a.shape)
print(a.dtype)

# ndim属性：给出数组的维度
print(a.ndim)

# size属性：返回数组元素的总个数
print(a.size)

# itemsize属性：返回数组中的元素在内存中所占用的字节数
print(a.itemsize)

# 数组占用的总字节数
# 方法1，nbytes
print(a.nbytes)

# 方法2，itemsize * size
print(a.itemsize * a.size)

# T属性，效果与transpose函数相同

print(a.T)

# 对于一维数组，T属性值就是原数组
b = arange(16)
print(b)
print(b.T)

