import numpy as np
import matplotlib.pyplot as plt
def square_sigma_sin(x, n):
    """将n个三角波函数合成为方波的近似函数"""
    sum1 = 0
    for a in range(1, 2*n, 2):
        sum1 += 1 / a * np.math.sin(a * x)
    return sum1

N = 200                                                           # N个采样点
input_value = [4 * np.math.pi * x / N for x in range(1, N + 1)]      # 输入列表，两个周期，将4pi分为N份
output_value = [square_sigma_sin(x, 9) for x in input_value]      # 输出列表，将输入带入到近似函数

plt.title("Square Function", fontsize=24)
plt.axis([0, 4 * np.math.pi, -2, 2])
plt.xlabel("input", fontsize=16)
plt.ylabel("output", fontsize=16)
plt.tick_params(axis="both", labelsize=16)
plt.scatter(input_value, output_value, c=output_value, cmap=plt.cm.Set2, s=20)
plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()
