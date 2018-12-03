# NumPy数组--自定义数据类型
from numpy import *
#  int8 int16 int32  int64   float32（单精度）、float64（双精度）或float
# bool
a = array([["a",1,2],[3,4,5],[6,7,8]])
print(a)
t = dtype([('name',str_,20),('age',int8),('salary', float32),('sex',bool)])

#b = array([("a",1,2),(3,4,5),(6,7,8)],dtype=t)
#print(b)

items = array([("Bill", 30, 1234),('Mary',54,5422.5)])
print(items)
items1 = array([("Bill", 30, 1234,1),('Mary',54,5422.5,0)],dtype=t)
print(items1)
