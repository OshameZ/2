import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']= 'SimHei'
%matplotlib inline
data1 = pd.read_excel('meal_order_detail.xlsx',sheet_name='meal_order_detail1')
data2 = pd.read_excel('meal_order_detail.xlsx',sheet_name='meal_order_detail2')
data3 = pd.read_excel('meal_order_detail.xlsx',sheet_name='meal_order_detail3')
# 2.数据预处理（NA）等处理，分析数据
data = pd.concat([data1,data2,data3],axis=0)
data.info()
data.dropna(axis=1,inplace=True)
#7.一天中什么时间段点菜梁集中
data['hourcount']= 1
data['time']=pd.to_datatime(data['place_order_time'])
data['hour'] = data['time'].map(lambda x:x.hour)
gp_by_hour = data.groupby(by='hour').count()['hourcount']
gp_by_hour.plot(kind='bar')
plt.xlabel('小时')
plt.ylabel('下单数量')
plt.title('下单量与小时数的关系')
#8.哪一天订餐数量多
data['daycount']= 1
data['day'] = data['time'].map(lambda x:x.day)
gp_by_day = data.groupby(by='day').count()['daycount']
gp_by_day.plot(kind='bar')
plt.xlabel('号')
plt.ylabel('下单数量')
plt.title('下单量与日期的关系')