import numpy as np


x = [1,2,3,4]
y = [5,6,7,8]
z = [11,22,33,44]
qwe = np.array((x,y,z), dtype=complex)
print(qwe)
a = np.arange(15).reshape(3,5)
print(a)



print(np.arange(10000).reshape(100, 100))