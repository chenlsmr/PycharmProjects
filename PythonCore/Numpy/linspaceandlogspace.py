import numpy as np
# 类似于matlab
a1 = np.linspace(0,10,7)
# 生成首位是0，末位是10，含7个数的等差数列
print(a1)
a = np.ones(3, dtype=np.int32)
b = np.linspace(0, np.pi, 3)

print(b.dtype.name)
c = a+b
print(c)
print(c.dtype.name)
d = np.exp(c*1j)
print(d)
print(d.dtype.name)

