# NumPy高级函数：计算两只股票的相关性
from numpy import *

# 相关性:两个数组之间的相关性
# 数组的相关性：如果将数组中的值绘制成两条曲线，
# 那么这两条曲线的趋势就是这两个数组的相关性

a = array([121.836,124.332,122.928,121.29,122.109,120.107,119.743,120.068,119.288,122.083,122.98,121.251,122.759,124.826,124.488,122.811,122.642,119.886,114.803,116.467,115.726,113.035,110.344,113.594,115.128,116.467,115.323,117.026,118.638,117.871])
b = array([44.681,45.669,45.682,45.903,46.241,45.539,43.472,44.122,44.473,44.551,44.499,43.888,44.616,45.331,44.85,43.199,43.277,42.744,41.483,41.821,42.172,41.483,40.352,40.963,41.782,42.146,41.925,42.51,42.068,42.042])

b = b * 3
# 相关性（系数）被定义为协方差除以各自的标准差的乘积
# 相关性的范围：-1到1之间
print(corrcoef(a,b))

from matplotlib.pyplot import *
t = arange(len(a))
plot(t,a,lw = 1)
plot(t,b,lw = 2)
show()



