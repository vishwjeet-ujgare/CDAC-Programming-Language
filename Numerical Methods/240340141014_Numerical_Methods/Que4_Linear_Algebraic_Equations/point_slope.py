import matplotlib.pyplot as plt

#list to stoe x and y 
x_new = []
y_new = []

for x in range(-10,10):
    y = 3 + 6 * (x-2)
    x_new.append(x)
    y_new.append(y)
    
# Create the plot
plt.plot(x_new,y_new)
    
# Add title and labels
plt.title('Graph of y = 3 + 6 * (x-2)')
plt.xlabel('x')
plt.ylabel('y')

# Show the plot
plt.show()   
