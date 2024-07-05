#Write a python code for Simpson’s ⅓ Rules. to calculate integration ∫(𝑥=0 to 1.5) 𝑓(𝑥)𝑑𝑥 if 𝑓(𝑥)=2+2𝑥+𝑥^2+sin⁡(2𝜋𝑥)+cos⁡(2𝜋𝑥/0.5) 

import numpy as np

def f(x):
    y = 2 + 2*x + x**2 + np.sin(2*np.pi*x) + np.cos(2*np.pi*x/0.5)
    return y

def simpson_rule(f, a, b, n):
    h = (b - a) / n
    sum = f(a) + f(b)
    for i in range(1, int(n/2 - 1) + 1):
        sum += 2 * f(a + 2 * i * h)
    for i in range(1, int(n/2) + 1):
        sum += 4 * f(a + (2 * i - 1) * h)
    return h/3 * sum

a = 0
b = 1.5
n = 10 #intervals

result = simpson_rule(f, a, b, n)
print("The integral value is:", result)
