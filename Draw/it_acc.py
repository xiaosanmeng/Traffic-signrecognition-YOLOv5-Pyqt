import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.size'] = '20'
plt.rcParams['font.sans-serif'] = ['SimHei']



df=pd.read_csv("../runs_label/train/exp9/results.csv")
# print(df.head())#显示前5行，从0行开始)
epoch = list(df['               epoch'])
accuracy_train = list(df['   metrics/precision']) # 训练集
accuracy_val = list(df['      metrics/recall']) # 验证集
plt.figure()
plt.plot(epoch, accuracy_train, c='red', label="train")
plt.plot(epoch, accuracy_val, c='blue', label="val")
plt.legend(loc='best')
plt.xlabel("epoch")
plt.ylabel("accuracy")
plt.show()