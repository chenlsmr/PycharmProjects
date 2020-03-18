import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("../input/car_crashes.csv")
data = data.corr()
sns.heatmap(data)
plt.show()
