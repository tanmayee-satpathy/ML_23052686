import numpy as np

x = np.array([1,3,4,2,5])
y = np.array([3,4,5,2,1])

b = np.sum((x - x.mean()) * (y - y.mean())) / np.sum((x - x.mean()) ** 2)
a = y.mean() - b * x.mean()

print("a : " , a)
print("b : " , b)