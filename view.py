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
#4.订单点菜的种类最多
data_group= data['order_id'].value_counts()[:10]
data_group.plot(kind='bar',fontsize=16,color=['r','m','b','y','g'])
plt.title('订单点菜的种类Top10')
plt.xlabel('订单Id',fontsize=16)
plt.ylabel('点菜种类',fontsize=16)
#5.订单id点菜数量top10
data['total_amounts'] =data['counts']*data['amounts']
dataGroup = data[['order_id','counts','amounts','total_amounts']].groupby(by='order_id')
Group_sum = dataGroup.sum()
sort_counts= Group_sum.sort_values(by='counts',ascending=False)
sort_counts['counts'][:10].plot(kind = 'bar', fontsize=16)
plt.xlabel('订单Id',fontsize=16)
plt.ylabel('点菜数量',fontsize=16)
plt.title('订单id点菜数量top10')
#6.消费金额前十名
sort_total_amounts= Group_sum.sort_values(by='total_amounts',ascending=False)
sort_total_amounts['total_amounts'][:10].plot(kind = 'bar', fontsize=16)
