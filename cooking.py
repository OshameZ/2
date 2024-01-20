import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']= 'SimHei'
%matplotlib inline
# 1.加载数据
data1 = pd.read_excel('meal_order_detail.xlsx',sheet_name='meal_order_detail1')
data2 = pd.read_excel('meal_order_detail.xlsx',sheet_name='meal_order_detail2')
data3 = pd.read_excel('meal_order_detail.xlsx',sheet_name='meal_order_detail3')
# 2.数据预处理（NA）等处理，分析数据
data = pd.concat([data1,data2,data3],axis=0)
data.info()
data.dropna(axis=1,inplace=True)
#统计卖出菜品的平均价格
round(data['amounts'].mean(),2)
#频数统计 什么菜最受欢迎（对菜名进行频数统计，排出前十名）
dishes_count = data['dishes_name'].value_counts()

# 3.数据可视化matplotlib
dishes_count.plot(kind='bar')
for x,y in enumerate(dishes_count):
    print(x,y)
    plt.text(x,y,y,ha='center',fontsize=12)
#


