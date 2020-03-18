import matplotlib.pyplot as plt
import tensorflow as tf

name_list = ['1', '2', '3']
num_list = [574.0, 320.0, 400]
plt.bar(range(len(num_list)), num_list, color='rgb',width=0.2, tick_label=name_list) #width来调整柱的宽度 color来设置颜色
plt.show()
