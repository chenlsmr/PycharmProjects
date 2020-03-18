import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Windows系统设置中文字体
import pd as pd
import seaborn as sns

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_csv("/冠状病毒谣言数据.csv")
#data = pd.read_csv("E:\Python\PycharmProjects\PythonCore\Climbing coronavirus rumor news for data analysis/冠状病毒谣言数据.csv")
df = pd.Series([j for i in [eval(i) for i in data["tag"].tolist()] for j in i]).value_counts()[:20]
X = df.index.tolist()
y = df.values.tolist()
plt.figure(figsize=(15, 8))  # 设置画布
plt.bar(X, y, color="orange")
plt.tight_layout()
# plt.grid(axis="y")
plt.grid(ls='-.')
plt.show()
