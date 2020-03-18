import numpy as np
a = "abcdef"
b = np.fromstring(a,dtype=np.int8)# 因为一个字符为8位，所以指定dtype为np.int8
print(b) # 返回 [ 97  98  99 100 101 102]