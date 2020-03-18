import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df_iris = pd.read_csv('../input/iris.csv')
fig, axes = plt.subplots(1,2)
sns.distplot(df_iris['petal length'], ax=axes[0], kde=True, rug=True)        # kde 密度曲线  rug 边际毛毯
sns.kdeplot(df_iris['petal length'], ax=axes[1], shade=True)                     # shade  阴影
plt.show()
