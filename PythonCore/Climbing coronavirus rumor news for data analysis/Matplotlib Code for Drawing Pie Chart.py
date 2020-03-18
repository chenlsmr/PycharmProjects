import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Windows系统设置中文字体
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# data = pd.read_csv("/冠状病毒谣言数据.csv")
data = pd.read_csv("E:\Python\PycharmProjects\PythonCore\Climbing coronavirus rumor news for data analysis/冠状病毒谣言数据.csv")
labels = data["explain"].value_counts().index.tolist()
sizes = data["explain"].value_counts().values.tolist()
colors = ['lightgreen', 'gold', 'lightskyblue', 'lightcoral']
plt.figure(figsize=(15,8))
plt.pie(sizes, labels=labels,
        colors=colors, autopct='%1.1f%%', shadow=True, startangle=50)# shadow=True 表示阴影
plt.axis('equal')#使图居中
plt.show()
