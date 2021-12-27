#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as mp
import pandas as pd
data = pd.read_csv('data_clean_zql.csv',header = 0)
print(data.head())
print(data.iloc[[0],[3]].isnull()==True)


# In[2]:


#去掉不用的列
data2=data.drop(columns=['用户的性别','投稿时间','tag的类型 new_channel还是old_channel'])
data2.head()


# In[3]:


#大会员变成0、1；因为这里对于空值的处理有问题，如果为年度大会员也会识别为空然后变成0，所以先把所有会员变为1，然后把
#非1处变为0
data2.loc[data2['vip']=='年度大会员','vip']=1
data2.loc[data2['vip']=='大会员','vip']=1
data2.loc[data2['vip']=='十年大会员','vip']=1
for i in range(data2.shape[0]):
    if data2.iloc[[i],[5]].values.flatten()!= 1:
        data2.iloc[[i],[5]]=0
data2.iloc[[740],[5]]
# data_nan = data2.loc[720:730,["vip"]]
# data_nan.head()
# if data2.iloc[[1],[5]].isna:
#     data2.iloc[[1],[5]]=0
# data_nan.fillna(0)
# data_nan.head()
#print((not data2.iloc[[1],[5]]==1))
#data2.head()


# In[4]:


data2.head()


# In[5]:


#去掉万
data2.iloc[[0],[19]]
for j in range(16,20):
    for i in range(data2.shape[0]):
        if(data2.iloc[i].iat[j][-1]=='万'):
            data2.iloc[[i],[j]] = float(data2.iloc[i].iat[j][0:-1])*10000


# In[6]:


data2.iloc[259].iat[18]


# In[7]:


#计算每个用户收藏视频总数
data3 = data2.loc[:,['用户的id','收藏夹id','视频数量']]
data4 = data3.drop_duplicates(subset='收藏夹id')
#data4.head()
data4['收藏夹总视频数'] = data4[['用户的id','视频数量']].groupby(by='用户的id').transform(lambda x:x.sum())
#data4.head()
data5=data4.drop_duplicates(subset='用户的id')
data5=data5.drop(columns=['收藏夹id','视频数量'])
data5.head()

# for i in range(data5.shape[0]):
#     current_id = data5.iloc[[i],[0]].values.flatten()
#     current_id[i]
    #data6.loc[current_id[i],'收藏夹总视频数']=data5.iloc[[i],[3]]


# In[8]:


data6=data5

data6.head()
data7=pd.merge(data2,data6)
data7.head()


# In[9]:


import numpy as np
l = data7['用户的签名（0,1）'].tolist()
for i in range(len(l)):
    if type(l[i]) == str:
        l[i]=1
    else:
        l[i] = 0
for i in range(len(l)):
    data7.iloc[[i],[2]] = l[i]
data7.head()        


# In[10]:


data2.iloc[0].iat[24][-1]


# In[11]:


data8=data7
data8.shape
#去掉万
for i in range(data8.shape[0]):
    if(data8.iloc[i].iat[24][-1]=='万'):
        data8.iloc[[i],[24]] = float(data8.iloc[i].iat[24][0:-1])*10000


# In[12]:


data8.to_csv('cleaned_data',index=False,encoding='utf_8_sig')

