#write a python code to line plot guessed value and error {guess**3-cube}. Please label the axis and lines.

import numpy as np
import matplotlib.pyplot as plt

# Define the cube value
cube = 27

# Generate guessed values using numpy linspace
guess = np.linspace(0, 30, 100)

# Calculate the error as (guess^3 - cube)
error = guess**3 - cube

# Create a line plot with labeled axes and legend
plt.plot(guess, error, label='Error = Guess^3 - Cube')
plt.xlabel('Guessed Value')
plt.ylabel('Error')
plt.legend()

# Display the plot
plt.show()