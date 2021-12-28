import pandas as pd
import numpy as np
import torch
from torch.functional import F
from sklearn import metrics

torch.set_default_tensor_type(torch.FloatTensor)
# data
data = pd.read_csv('alldata_eachUser.csv')
# 去掉用户id
trainingSet = data.iloc[:, 1:]
trainingData = trainingSet.drop(columns='vip')
X = np.array(trainingData)
y = trainingSet.iloc[:, 6]


class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden_1 = torch.nn.Linear(n_feature, n_hidden)
        self.hidden_2 = torch.nn.Linear(n_hidden, 128)
        self.hidden_3 = torch.nn.Linear(128, 32)
        self.predict = torch.nn.Linear(32, n_output)

    def forward(self, x_input):
        x_input = F.relu(self.hidden_1(x_input))
        x_input = F.relu(self.hidden_2(x_input))
        x_input = F.relu(self.hidden_3(x_input))
        x_predict = self.predict(x_input)
        return x_predict


X = torch.FloatTensor(X)
y = torch.LongTensor(y)
net = Net(41, 256, 2)
opt = torch.optim.SGD(net.parameters(), lr=0.0125)
loss_func = torch.nn.CrossEntropyLoss()

# train
for step in range(2000):
    out = net(X)
    loss = loss_func(out, y)
    opt.zero_grad()
    loss.backward()
    opt.step()
    if (step + 1) % 10 == 0:
        prediction = torch.max(F.softmax(out, dim=1), 1)[1]
        pred_y = prediction.data.numpy().squeeze()
        target_y = y.data.numpy()
        fpr, tpr, thresholds = metrics.roc_curve(target_y, pred_y, pos_label=1)
        AUC = metrics.auc(fpr, tpr)
        print('epoch ', step + 1, ' AUC:', AUC)
        pass
