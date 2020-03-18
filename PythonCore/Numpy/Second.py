import numpy as np
a = np.arange(15).reshape(3,5)
a1 = np.array([2,3,4])
a2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
b = np.array([1.2,3.5,5.1])
b2 = a2[a2>6] #截取矩阵a中大于6的元素，返回的是一维数组
print(b2) #返回[ 7  8  9  10]
c = np.array([[1,2,3,4,5],[6,7,8,9,10]])
#print(a)
#print(a.shape)
#print(a.ndim) #数组轴的个数，在python的世界中，轴的个数被称作秩
#print(a.dtype.name)
#print(a.itemsize)# 数组中的每个元素的字节大小
#print(a.size)
#print(type(a))
#print(a1)
#print(a1.dtype)
print(a2[0:1]) # 截取第一行,返回 [[1 2 3 4 5]]
print(a2[1,2:5]) # 截取第二行，第三、四、五列，返回 [8 9 10]
print(a2[1,:]) # 截取第二行,返回 [6 7 8 9 10]
#print(b)
#print(type(b))
#print(b.dtype)# 浮点类型
#print(c.shape)# 结果返回一个tuple元组 (2, 5) 2行，5列
#print(c.shape[0])# 获得行数，返回 2
#print(c.shape[1])# 获得列数，返回 5