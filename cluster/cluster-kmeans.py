#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')
data = pd.read_csv('alldata_eachUser.csv')
data


# In[75]:


#标准化处理
train_data = data.drop(columns=['用户的id','保密','男','女'])
from sklearn.preprocessing import MinMaxScaler
MMS = MinMaxScaler()
train_data = MMS.fit_transform(train_data)
train_data = pd.DataFrame(train_data,columns = list(train_data))
train_data = train_data.values


# In[76]:


import numpy as np
from scipy.spatial.distance import pdist, euclidean
#train_data = train_data.values
SSE =[]
DBI=[]
n = 20
for k in range(2,n):
    model = KMeans(n_clusters=k, init='k-means++', n_init=50, max_iter=500, tol=0.001,   
         precompute_distances='auto', verbose=0, random_state=None,  
         copy_x=True, n_jobs=None, algorithm='auto')
    model.fit(train_data)
    pred = np.array(model.predict(train_data).astype(int))
    SSE.append(model.inertia_)

#     print(pred[500])
#     print(type(pred[0]))
    #labels=pred.astype('int64')
    n_cluster = len(np.bincount(pred)) #质心的数量， np.bincount()去非负不重复的整数数组
    print(n_cluster,end=" ")
    cluster_k = [train_data[pred==k]for k in range(n_cluster)]
    #print(cluster_k)
    centroids = [np.mean(k, axis=0) for k in cluster_k]
    S = [np.mean([euclidean(p,centroids[i]) for p in k]) for i,k in enumerate(cluster_k)]
    Ri = []
    for i in range(n_cluster):
        Rij = []
        #衡量第i类与第j类的相似度
        for j in range(n_cluster):
            if j!=i:
                r = (S[i]+S[j])/euclidean(centroids[i],centroids[j])  #这个分母是Mij，即两个质心的距离
                Rij.append(r)
        Ri.append(max(Rij))
    dbi = np.mean(Ri)
    DBI.append(dbi)
import matplotlib.pyplot as plt
#显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(i)
#plt.plot(range(2,n),SSE)
plt.xlabel('簇数量——聚类的k值')
plt.ylabel('簇的DBI')
plt.plot(range(3,n),DBI[1:])
plt.show()


# In[4]:


#k = 8进行聚类
data['c_kmeans'] = KMeans(n_clusters=8).fit(train_data).predict(train_data)
data.to_csv('user_category_kmeans.csv',index = False,encoding='utf_8_sig')


# In[77]:


from sklearn.manifold import TSNE

tsne = TSNE(n_components=3, perplexity=30, early_exaggeration=4.0, 
            learning_rate=100, n_iter=2000, n_iter_without_progress=30, 
            min_grad_norm=1e-07, metric='euclidean', init='random',
            verbose=0, random_state=None, method='barnes_hut', angle=0.5)
result = tsne.fit_transform(train_data)
result[0]
plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.scatter3D(result[:,0], result[:,1], result[:,2], cmap='Greens')

