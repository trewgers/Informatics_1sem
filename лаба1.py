import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


theta_deg = [
    29.3, 29.3, 29.3,
    33.0, 33.0, 33.0,
    35.8, 35.8, 35.8,
    38.1, 38.1, 38.1,
    40.7, 40.7, 40.7,
    44.8, 44.8, 44.8,
    48.0, 48.0, 48.0,
    51.1, 51.1, 51.1,
    54.3, 54.3, 54.3,
    57.6, 57.6, 57.6
]

A = [
    2.06, 2.01, 2.01,
    2.78, 2.55, 2.63,
    3.24, 3.23, 3.17,
    3.31, 3.54, 3.26,
    3.99, 4.08, 3.84,
    4.42, 4.68, 4.52,
    5.09, 5.01, 5.08,
    5.43, 5.58, 5.61,
    5.98, 5.99, 6.21,
    6.61, 6.48, 6.37
]

n = len(theta_deg)
print(f"Всего точек: {n}")

theta_rad = np.radians(theta_deg)
x = np.tan(theta_rad)
y = np.array(A) / np.cos(theta_rad)

result = stats.linregress(x, y)
a_slope = result.slope
b_intercept = result.intercept
r2 = result.rvalue**2

a_err = result.stderr
b_err = result.intercept_stderr



print(f"Уравнение: y = {a_slope:.6f}·x + {b_intercept:.6f}")
print(f"a = {a_slope:.6f} ± {a_err:.6f}")
print(f"b = {b_intercept:.6f} ± {b_err:.6f}")
print(f"R² = {r2:.6f}")



x_fit = np.linspace(min(x), max(x), 100)
y_fit = a_slope * x_fit + b_intercept

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='red', s=50, alpha=0.7, label='Значения')
plt.plot(x_fit, y_fit, color='black', linewidth=2,
         label=f'y = {a_slope:.4f}·x + {b_intercept:.4f}')

plt.xlabel('x = tg(θ)', fontsize=12)
plt.ylabel('y = A / cos(θ)', fontsize=12)
plt.title('График ', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()


y_pred = a_slope * x + b_intercept
residuals = y - y_pred
s2 = np.sum(residuals**2) / (n - 2)

x_mean = np.mean(x)
a_err_classic = np.sqrt(s2 / np.sum((x - x_mean)**2))
b_err_classic = np.sqrt(s2 * (1/n + x_mean**2 / np.sum((x - x_mean)**2)))

print("\nПроверка (классические формулы МНК):")
print(f"a = {a_slope:.6f} ± {a_err_classic:.6f}")
print(f"b = {b_intercept:.6f} ± {b_err_classic:.6f}")
print(-b_intercept/a_slope)
print(((a_err_classic**2) * (x_mean **2))**1/2)
