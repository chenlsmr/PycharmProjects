import numpy as np
a_ones = np.ones((3,4)) # 创建3*4的全1矩阵
print(a_ones)
# 结果
np.ones((2,3,4), dtype=np.int16)   # dtype can also be specified
a_zeros = np.zeros((3,4))
# 创建3*4的全0矩阵
print(a_zeros)
# 结果

a_eye = np.eye(3)
# 创建3阶单位矩阵
print(a_eye)
# 结果

a_empty = np.empty((3,4))
# 创建3*4的空矩阵
print(a_empty)
# 结果
np.set_printoptions(threshold='nan')