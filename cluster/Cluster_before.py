#!/usr/bin/env python
# coding: utf-8

# In[31]:


#加载数据，并取视频信息列
import pandas as pd
data = pd.read_csv('final_data_toCluster.csv')
data.head(90000)
data2 = data.iloc[:,11:19]
data2.head()
data2.shape


# In[40]:


#离散化数据，等频分为30个区间（13万行样本）
# data2.head()
data3=[]
label = range(30)
for i in range(8):
    data3.append(pd.qcut(data2.iloc[:,[i]].values[:,0],30,labels=label))
for i in range(8):
    print(data3[i].value_counts())
# data4=data
# data4['视频的up主的粉丝数']=data3
# data4.head(90000)


# In[38]:


#用离散化的连续值替换原来的视频信息
data4 = data
for i in range(11,19):
    data4.iloc[:,[i]] = data3[i-11]
user_id = data4['用户的id'].drop_duplicates().values
data4.to_csv('mid1.csv',encoding='utf_8_sig')


# In[34]:


#接下来把所有大TAG切换为feature，值为该用户收藏夹出现该 TAG频次
#首先得到每个用户TAG频次字典
from collections import Counter
import numpy as np
tag_each_id = []
for i in user_id:
    to_dic = data5[data5['用户的id'] == i].iloc[:,[-1]].values.tolist()
    to_dic = np.array(to_dic)
    dic_tag = dict(Counter(to_dic[:,0]))
    #print(dict(dic_tag))
    tag_each_id.append(dic_tag)
tag_each_id[0]


# In[35]:


#把所有大TAG作为feature，频数作为值
#data6 = data5.drop('大Tag',axis=1).drop_duplicates(subset='用户的id')
#data6.index = range(len(data6))
print(data6.shape)
tag_set = data5['大Tag'].drop_duplicates().tolist()
tag_set
for i in tag_set:
    data6[i] = 0

i = 0
for j in tag_each_id:
#     print(j)
    for k in tag_set:
#         print(k)
#         print(k in j)
#         print(data6[k])
        if k in j:
            data6[k][i] = j[k]
    i = i + 1
        
data6
    


# In[67]:


data6.to_csv("alldata_eachUser.csv",encoding='utf_8_sig',index=False)

