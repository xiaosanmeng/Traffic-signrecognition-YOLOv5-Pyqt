import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.size'] = '20'
plt.rcParams['font.sans-serif'] = ['SimHei']



df=pd.read_csv("../result/results_yolov5.csv")
# print(df.head())#显示前5行，从0行开始)
epoch = list(df['               epoch'])
accuracy_val1 = list(df['        val/box_loss']) # 训练集
accuracy_train1 = list(df['      train/box_loss']) # 训练集
# accuracy_train2 = list(df['        val/obj_loss']) # 训练集
# accuracy_train3 = list(df['        val/cls_loss']) # 训练集
plt.figure()
plt.plot(epoch, accuracy_train1, c='red', linestyle='solid', label="训练集 train")
plt.plot(epoch, accuracy_val1, c='green', linestyle='dotted', label="验证集 validation")
plt.legend(loc='best')
plt.xlabel("训练轮次 epoch")
plt.ylabel("损失值 loss")
plt.show()