import numpy as np

x = np.array([-2,-1,0,1,2])
y = np.array([1,2,3,3,4])

b = np.sum((x - x.mean()) * (y - y.mean())) / np.sum((x - x.mean()) ** 2)
a = y.mean() - b * x.mean()

print("a : " , a)
print("b : " , b)