# Simple Linear Regression (manual)

x = list(map(int, input("Enter hours studied: ").split()))
y = list(map(int, input("Enter marks: ").split()))

n = len(x)

x_mean = sum(x) / n
y_mean = sum(y) / n

num = 0
den = 0

for i in range(n):
    num += (x[i] - x_mean) * (y[i] - y_mean)
    den += (x[i] - x_mean) ** 2

m = num / den
c = y_mean - m * x_mean

print("Slope (m):", m)
print("Intercept (c):", c)

xp = int(input("Enter hours to predict marks: "))
yp = m * xp + c

print("Predicted Marks:", yp)