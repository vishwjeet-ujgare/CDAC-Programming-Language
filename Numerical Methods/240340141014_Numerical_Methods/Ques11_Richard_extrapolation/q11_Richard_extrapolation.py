#Using Richardson Extrapolation method solve find f’(x3)=? With h=2,1
    # x 1, 2, 3, 4, 5, 6, 7
    # y 4, 6, 10, 18, 34, 66, 130
    # f’(x3) = (f(x3+h)-f(x3-h))/(2*h)
    
    
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([4, 6, 10, 18, 34, 66, 130])
h1 = 2
h2 = 1

f_prime_x3_h1 = (y[4]-y[2])/(2*h1)
f_prime_x3_h2 = (y[3]-y[2])/(2*h2)
f_prime_x3_richardson = f_prime_x3_h2 + (f_prime_x3_h2 - f_prime_x3_h1)/3


print("f'(x3) = ",f_prime_x3_richardson)
print("f'(x3) = ",f_prime_x3_h1)
print("f'(x3) = ",f_prime_x3_h2)
print("f'(x3) = ",f_prime_x3_richardson)