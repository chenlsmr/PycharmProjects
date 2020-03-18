import numpy as np
def func(i,j):
    return i+j

a = np.fromfunction(func,(5,6))
# 第一个参数为指定函数，第二个参数为列表list或元组tuple,说明矩阵的大小
print(a)
# 返回