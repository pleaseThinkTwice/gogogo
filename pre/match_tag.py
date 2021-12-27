#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
def small_to_big(small,data):
    l1 = data['每个小类的名'].values.tolist()
    l2 = data['19类每个类的名字'].values.tolist()
    _ = [i for i in range(len(l1)) if l1[i] == small]
    if len(_)==0:
        return "未知"
    else:
        return l2[_[0]]
data=pd.read_excel("19categories.xlsx")
#print(small_to_big("111",data))


# In[2]:


data1 = pd.read_csv('clean_data_z.csv')
data1.head()


# In[3]:


data2 = data1
for i in range(data2.shape[0]):
    s_tag = data2.iloc[[i],[26]].values[0][0]
    #print(s_tag)
    data2.iloc[[i],[-1]] = small_to_big(s_tag,data)
data2.head()


# In[16]:


data2.to_csv("final_all_data.csv",encoding='utf_8_sig')

