import numpy as np

x1 = np.array([3, 4, 5, 6, 2])
x2 = np.array([8, 5, 7, 3, 1])
y  = np.array([-3.7, 3.5, 2.5, 11.5, 5.7])

X = np.column_stack((np.ones(len(x1)), x1, x2))

beta = np.linalg.lstsq(X, y, rcond=None)[0]
b0, b1, b2 = beta

print("b0, b1, b2 =", beta)

x_new = np.array([1, 3, 2])
y_pred = x_new @ beta

print("Predicted y =", y_pred)
