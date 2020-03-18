import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("../input/iris.csv")
sns.set()                        #使用默认配色
sns.pairplot(data,hue="class")   #hue 选择分类列
plt.show()