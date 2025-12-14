x = [1, 2, 3, 4, 5]
y = [5, 6, 10, 13, 11]

b0 = 3
b1 = 2
lr = 0.1     
iterations = 10

n = len(x)

def compute_cost(b0, b1):
    cost = 0
    for i in range(n):
        yp = b0 + b1 * x[i]
        cost += (yp - y[i]) ** 2
    return cost / n

print("Iter |   b0     b1     Cost")
print("-------------------------------")

for it in range(iterations + 1):
    print(f"{it:4d} | {b0:.4f}  {b1:.4f}  {compute_cost(b0,b1):.4f}")

    sum_error_b0 = 0
    sum_error_b1 = 0

    for i in range(n):
        yp = b0 + b1 * x[i]
        error = y[i] - yp
        sum_error_b0 += error
        sum_error_b1 += x[i] * error

    db0 = -(2/n) * sum_error_b0
    db1 = -(2/n) * sum_error_b1
    b0 = b0 - lr * db0
    b1 = b1 - lr * db1
