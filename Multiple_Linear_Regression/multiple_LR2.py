import numpy as np

x1 = np.array([60, 62, 67, 70, 71, 72, 75, 78])
x2 = np.array([22, 25, 24, 20, 15, 14, 14, 11])
y  = np.array([140, 155, 159, 179, 192, 200, 212, 215])

X = np.column_stack((np.ones(len(x1)), x1, x2))

beta = np.linalg.lstsq(X, y, rcond=None)[0]
b0, b1, b2 = beta

print("b0, b1, b2 =", beta)

x_new = np.array([1, 80, 24])
y_pred = x_new @ beta

print("Predicted y =", y_pred)
