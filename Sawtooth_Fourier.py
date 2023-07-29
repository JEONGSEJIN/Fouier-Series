# Sawtooth Wave(톱니파) Signal - Fourier Series

import numpy as np
import matplotlib.pyplot as plt

# Sawtooth Wave Signal
def function(x):
    x_mod_period = x % (2 * np.pi)
    return np.where((0 < x_mod_period) & (x_mod_period < 2 * np.pi), (np.pi - x_mod_period)/2, (np.pi - x_mod_period)/2)

# 수치적분
def integrate(func, a, b, N=100):
    x = np.linspace(a, b, N)
    y = func(x)
    dx = (b - a) / N
    return np.sum(y) * dx

def fourier(x, n):
    period = 2 * np.pi
    a0 = 0.0
    an = np.zeros(n)
    bn = np.zeros(n)
    
    for i in range(1, n + 1):    # 푸리에 계수
        integrand_cos = lambda x: function(x) * np.cos(i * x)
        integrand_sin = lambda x: function(x) * np.sin(i * x)
        an[i - 1] = (1 / np.pi) * integrate(integrand_cos, 0, period)
        bn[i - 1] = (1 / np.pi) * integrate(integrand_sin, 0, period)
        
    sum = a0 / 2
    for i in range(n):
        sum += an[i] * np.cos((i + 1) * x) + bn[i] * np.sin((i + 1) * x)
    return sum

#A = np.pi / 2
num_terms = 10    # 4, 8, 20
x_values = np.linspace(0, 6 * np.pi, 100)
fourier_approxi = [fourier(x, num_terms) for x in x_values]

plt.plot(x_values, fourier_approxi, label=f"Fourier Approximation (n={num_terms})")
plt.plot(x_values, [function(x) for x in x_values], label="Sawtooth Function", linestyle="--")
plt.legend(loc="lower left")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Fourier Series Approximation")
plt.show()
