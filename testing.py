import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def curve_func(x, a, b, c):
    return a * np.exp(-b * x) + c


data = []
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

n = []
divAndConTime = []
bruteforceTime = []
for row in data:
    n.append(float(row['n']))
    divAndConTime.append(float(row['divAndConTime']))
    bruteforceTime.append(float(row['bruteforceTime']))

mean_divAndConTime = np.mean(divAndConTime)
variance_divAndConTime = np.var(divAndConTime)
std_dev_divAndConTime = np.std(divAndConTime)

mean_bruteforceTime = np.mean(bruteforceTime)
variance_bruteforceTime = np.var(bruteforceTime)
std_dev_bruteforceTime = np.std(bruteforceTime)





params, _ = curve_fit(curve_func, n, divAndConTime)
x_curve = np.linspace(min(n), max(n), 600)
y_curve = curve_func(x_curve, *params)
plt.scatter(n, divAndConTime, label='divAndConTime')



params, _ = curve_fit(curve_func, n, bruteforceTime)
x_curve = np.linspace(min(n), max(n), 100)
y_curve = curve_func(x_curve, *params)
plt.scatter(n, bruteforceTime, label='bruteforceTime')

plt.xlabel('n')
plt.ylabel('time in sec')
plt.title('Closest pair problem')
plt.legend()
plt.grid(True)
plt.show()
