# import numpy as np
# import matplotlib.pyplot as plt

# # Create an array of x values
# x = np.linspace(-10, 10, 400)

# # Calculate the corresponding y values
# y = 3 - 2*x

# # Create the plot
# plt.plot(x, y)

# # Add title and labels
# plt.title('Graph of y + 2x = 3')
# plt.xlabel('x')
# plt.ylabel('y')

# # Show the plot
# plt.show()


import matplotlib.pyplot as plt
from math import tan
# Initialize empty lists to store x and y values
x_values = []
y_values = []

# Loop to generate x and y values
for x in range(-50, 50):  # loop from -10 to 10
    y = 3 - 2 *tan(x)
    x_values.append(x)  # add x to the list
    y_values.append(y)  # add y to the list

# Create the plot
plt.plot(x_values, y_values)

# Add title and labels
plt.title('Graph of y = 3 - 2x')
plt.xlabel('x')
plt.ylabel('y')

# Show the plot
plt.show()