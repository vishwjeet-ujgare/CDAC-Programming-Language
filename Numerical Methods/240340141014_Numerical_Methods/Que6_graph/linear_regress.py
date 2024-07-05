# 6) Use for loop to calculate (num / den) or (Yi-Ymean) for each iteration of Linear Regression.
# Plot a graph of error to show it’s progresses with iteration.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12.0, 9.0)

# Preprocessing Input data
data = {'A': [4  , 5  , 5  , 6  , 7  , 8, 8  , 9],
        'B': [4.5, 4.5, 5.3, 5.7, 7.4, 8, 8.5, 8.5]}

data=pd.DataFrame.from_dict(data)

X = data.iloc[:, 0]
Y = data.iloc[:, 1]
plt.scatter(X, Y)
plt.show()

# Building the model
X_mean = np.mean(X)
Y_mean = np.mean(Y)
num = 0
den = 0

for i in range(len(X)):
    num += (X[i] - X_mean)*(Y[i] - Y_mean)
    den += (X[i] - X_mean)**2
m = num / den
c = Y_mean - m*X_mean
print (m, c)

# Making predictions
Y_pred = m*X + c
plt.scatter(X, Y) # actual
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red') # predicted

plt.show()