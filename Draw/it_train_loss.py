import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.size'] = '20'
plt.rcParams['font.sans-serif'] = ['SimHei']



df=pd.read_csv("../runs/train/exp15/results.csv")
# print(df.head())#显示前5行，从0行开始)
epoch = list(df['               epoch'])
accuracy_train1 = list(df['      train/box_loss']) # 训练集
accuracy_train2 = list(df['      train/obj_loss']) # 训练集
accuracy_train3 = list(df['      train/cls_loss']) # 训练集
plt.figure()
plt.plot(epoch, accuracy_train1, c='red', label="box_loss")
plt.plot(epoch, accuracy_train2, c='blue', label="obj_loss")
plt.plot(epoch, accuracy_train3, c='green', label="cls_loss")
plt.legend(loc='best')
plt.xlabel("epoch")
plt.ylabel("accuracy")
plt.show()