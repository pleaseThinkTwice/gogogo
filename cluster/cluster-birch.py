#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')
data = pd.read_csv('alldata_eachUser.csv').drop(columns=['用户的id','保密','男','女'])
data


# In[27]:


#标准化处理
train_data = data
from sklearn.preprocessing import MinMaxScaler
MMS = MinMaxScaler()
train_data = MMS.fit_transform(train_data)
train_data = pd.DataFrame(train_data,columns = list(data)).values
train_data


# In[45]:


from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
tsne = TSNE(n_components=3, perplexity=30, early_exaggeration=4.0, 
            learning_rate=1000, n_iter=2000, n_iter_without_progress=30, 
            min_grad_norm=1e-07, metric='euclidean', init='random',
            verbose=0, random_state=None, method='barnes_hut', angle=0.5)
result = tsne.fit_transform(train_data)
ax = plt.axes(projection='3d')
ax.scatter3D(result[:,0], result[:,1], result[:,2], cmap='Greens')


# In[46]:


from sklearn.cluster import Birch
import numpy as np
import matplotlib.pyplot as plt
# coding='utf-8'
from sklearn.cluster import Birch
from time import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn.manifold import TSNE
def birch(data, tsnedata):
    X = data
    birch = Birch(n_clusters=8, threshold=0.8)#样本的方差较大，则一般需要增大这个默认值。
    #threshold:即叶节点每个CF的最大样本半径阈值T，它决定了每个CF里所有样本形成的超球体的半径阈值。
    ##训练数据
    labels = birch.fit_predict(X)
    print(tsnedata[labels])
    plt.scatter(tsnedata[:, 0], tsnedata[:, 1], c=labels)
    plt.show()
    from collections import Counter
    print(Counter(labels))

    colors = ['b', 'g', 'r', 'k', 'c', 'm', 'y', '#e24fff', '#524C90', '#845868']

    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot(111)
    #print(tsnedata[labels == 1][1])
    x_min, x_max = np.min(tsnedata, 0), np.max(tsnedata, 0)
    tsnedata = (tsnedata - x_min) / (x_max - x_min)
    #print(tsnedata)
    pd.DataFrame(tsnedata[labels == 0]).plot(x=0, y=1, kind="scatter", label="聚类标签 0", color=colors[0],
                               fontsize=12, ax=ax,
                               )
    pd.DataFrame(tsnedata[labels == 1]).plot(x=0, y=1, kind="scatter", label="聚类标签 1", color=colors[1],
                               fontsize=12, ax=ax,
                               )
    pd.DataFrame(tsnedata[labels == 2]).plot(x=0, y=1, kind="scatter", label="聚类标签 2", color=colors[2],
                               fontsize=12, ax=ax,
                               )
    pd.DataFrame(tsnedata[labels == 3]).plot(x=0, y=1, kind="scatter", label="聚类标签 3", color=colors[3],
                               fontsize=12, ax=ax,
                               )
    pd.DataFrame(tsnedata[labels == 4]).plot(x=0, y=1, kind="scatter", label="聚类标签 4", color=colors[4],
                               fontsize=12, ax=ax,
                               )
    pd.DataFrame(tsnedata[labels == 5]).plot(x=0, y=1, kind="scatter", label="聚类标签 5", color=colors[5],
                               fontsize=12, ax=ax,
                               )
    pd.DataFrame(tsnedata[labels == 6]).plot(x=0, y=1, kind="scatter", label="聚类标签 6", color=colors[6],
                               fontsize=12, ax=ax,
                               )
    pd.DataFrame(tsnedata[labels == 7]).plot(x=0, y=1, kind="scatter", label="聚类标签 7", color=colors[7],
                               fontsize=12, ax=ax,
                               )
   # tsnedata[labels == 3].plot(x=0, y=1, kind="scatter", label="聚类标签 3", color=colors[3],
                               #fontsize=12, ax=ax,
                               #)

    ax.set_xlabel(" ", fontsize=14)
    ax.set_ylabel(" ", fontsize=14)
    plt.savefig('聚类结果散点图.svg')


# In[47]:


birch(train_data,result)


# In[49]:


from sklearn.cluster import Birch
import numpy as np
import matplotlib.pyplot as plt
# coding='utf-8'
from sklearn.cluster import Birch
from time import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn.manifold import TSNE
from sklearn import metrics
def birch(data,n,threshold):
    X = data
    birch = Birch(n_clusters=n, threshold=threshold)#样本的方差较大，则一般需要增大这个默认值。
    #threshold:即叶节点每个CF的最大样本半径阈值T，它决定了每个CF里所有样本形成的超球体的半径阈值。
    ##训练数据
    labels = birch.fit_predict(X)
    return metrics.calinski_harabasz_score(X, labels)


# In[50]:


CH = []
cluter_n = range(3,20)
for i in cluter_n:
    CH.append(birch(train_data,i,0.8))
print(CH)
plt.plot(cluter_n,CH)
plt.xlabel('the number of cluster')
plt.ylabel('calinski_harabasz_score')
plt.show()


# In[59]:


#k = 8进行聚类（选3、4也可）
data['category_by_birch'] = Birch(n_clusters=8, threshold=0.8).fit_predict(train_data)
data.to_csv('user_category_birch.csv',index = False,encoding='utf_8_sig')

