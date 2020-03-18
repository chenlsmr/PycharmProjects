# Seaborn下的频次直方图
from plotly.express import pd
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.figure_factory import np
data = np.random.multivariate_normal([0, 0], [[5,2],[2,2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])
for col in 'xy':
    plt.hist(data[col], density=True, alpha=0.5)
