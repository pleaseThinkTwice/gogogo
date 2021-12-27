#!/usr/bin/env python
# coding: utf-8

# In[85]:


import pandas as pd
import numpy as np
data = pd.read_csv("cleaned_data.csv")
data.head()


# In[86]:


data2 = data
df = data[['用户的等级','关注数','粉丝数','收藏夹总视频数','视频的收藏数','视频的播放数','视频的弹幕数',
          '点赞数','投币数','分享数','视频的up主的粉丝数','标签的订阅数',
           '这个标签下的视频投稿数','这个标签下的精选视频数']]
cols_level=list(df['用户的等级'])   # 可以改成自己需要的列的名字
cols_foll=list(df['关注数'])
cols_befoll=list(df['粉丝数'])
cols_setNum=list(df['收藏夹总视频数'])
cols_VedioSeted=list(df['视频的收藏数'])
cols_played=list(df['视频的播放数'])
cols_danmu=list(df['视频的弹幕数'])
cols_good=list(df['点赞数'])
cols_coin=list(df['投币数'])
cols_shared=list(df['分享数'])
cols_upFans=list(df['视频的up主的粉丝数'])
cols_tagFans=list(df['标签的订阅数'])
cols_tagVedio=list(df['这个标签下的视频投稿数'])
cols_tagBest=list(df['这个标签下的精选视频数'])
cols=[cols_level,cols_foll,cols_befoll,cols_setNum,cols_VedioSeted,cols_played,cols_danmu,cols_good,
     cols_coin,cols_shared,cols_upFans,cols_tagFans,cols_tagVedio,cols_tagBest]
df
# for i in range(len(cols[0])):
#     item = cols[i]
#     #item = [j[i] for j in cols]
#     print(item[0])
#     mean_tmp = np.mean(np.array(item))
#     std_tmp = np.std(np.array(item))
#     if(std_tmp):
#          df[i] = df[i].apply(lambda x: (x - mean_tmp) / std_tmp)
# df.head()


# In[87]:


# 标准化处理(转化为均值为0，标准差为1 附近的值)
from sklearn.preprocessing import StandardScaler  #归一化库 
#2.实例化一个转换器类
transfer = StandardScaler() 
#3.#调用fit_transform()
xi = transfer.fit_transform(df) 
# print(xi) 
#4、转化为二维表
data4 = pd.DataFrame(xi,columns=df.columns)
#data["y"] = df['y']display(data.tail(3))
# data4.head(15)
data2['用户的等级']=data4['用户的等级']
data2['关注数']=data4['关注数']
data2['粉丝数']=data4['粉丝数']
data2['收藏夹总视频数']=data4['收藏夹总视频数']
data2['视频的收藏数']=data4['视频的收藏数']
data2['视频的播放数']=data4['视频的播放数']
data2['视频的弹幕数']=data4['视频的弹幕数']
data2['点赞数']=data4['点赞数']
data2['投币数']=data4['投币数']
data2['分享数']=data4['分享数']
data2['视频的up主的粉丝数']=data4['视频的up主的粉丝数']
data2['标签的订阅数']=data4['标签的订阅数']
data2['这个标签下的精选视频数']=data4['这个标签下的精选视频数']
data2['这个标签下的视频投稿数']=data4['这个标签下的视频投稿数']
data2.head()


# In[88]:


data2.to_csv('clean_data_z.csv',encoding='utf_8_sig')

