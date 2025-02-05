import matplotlib.pyplot as plt
import numpy as np
import time

def x(n):
    x = 1
    for i in range(n):
        for j in range(n):
            x = x + 1

n_values = np.arange(1, 1000, 20)
x_times = []

for n in n_values:
    start = time.time()
    x(n)
    end = time.time()
    x_times.append(end - start)


model = np.poly1d(np.polyfit(n_values, x_times, 2))
polyline = np.linspace(1, 1000, 3)

print(model)

plt.plot(n_values, x_times, 'bo', label='x(n)')
plt.plot(n_values, model(n_values), 'r-', label='quadratic')
plt.plot(n_values, np.poly1d([0.5e-8,0,0])(n_values), 'g-', label='lower bound: 0.5e-8*x^2')
plt.plot(n_values, np.poly1d([4e-8,0,0])(n_values), 'purple', label='upper bound: 4e-8*x^2')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('time vs. n')
plt.legend()
plt.grid(True)
plt.show()