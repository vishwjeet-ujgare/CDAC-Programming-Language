#write a program for y = 3 - 2 * x . add loop and make x and y list
import matplotlib.pyplot as plt 

# lists to store x and y values
x_new = []
y_new = []

# Loop to generate x and y values
for x in range(-10,20):  
    y = 3 - 2 * x 
    x_new.append(x)  # add x to the list
    y_new.append(y)  # add y to the list

# Create the plot
plt.plot(x_new, y_new)

# Add title and labels
plt.title('Graph of y = 3 - 2x')
plt.xlabel('x')
plt.ylabel('y')

# Show the plot
plt.show()   
