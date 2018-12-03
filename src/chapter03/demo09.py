# NumPy常用函数：根据日期分析股票涨幅
from numpy import *
from datetime import *
# take：返回索引对应的值组成的数组
# argmax：取数组中最大值对应的索引
# argmin：取数组中最小值对应的索引

'''
星期一：0
星期二：1
星期三：2
星期四: 3
星期五：4
星期六：5
星期日：6
'''
def datestr2num(s):
    return datetime.strptime(s.decode('utf-8'),'%d-%m-%Y').date().weekday()
#print(datestr2num(b'12-2-2016'))

dates,close = loadtxt('data.csv', delimiter=',', usecols=(1,6),unpack=True,
                      converters={1:datestr2num})
dates = dates.astype(int)
print('Dates','=',dates)

averages = zeros(5)
for i in range(5):
    indices = where(dates == i)
    prices = take(close, indices)
    avg = mean(prices)
    print("Day",i,"prices", prices,'平均值', avg)
    averages[i] = avg

top = max(averages)
print('最高收盘价:',top)
print('哪天收盘价最高：', argmax(averages))

bottom = min(averages)
print('最低收盘价：', bottom)
print('哪天收盘价最低',argmin(averages))




