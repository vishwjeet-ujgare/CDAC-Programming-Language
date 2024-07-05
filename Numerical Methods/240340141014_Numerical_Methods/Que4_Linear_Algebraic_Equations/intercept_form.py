import matplotlib.pyplot as plt

#intialize the list
x_new = []
y_new = []

#loop for the range
for x in range(-50,50):
    y = (1 - x/2) * 3
    x_new.append(x)
    y_new.append(y)
    
#create the plot
plt.plot(x_new, y_new)

#Add the titles
plt.title('Graph of y = 1 - x/2 * 3')
plt.xlabel('x')
plt.ylabel('y')

#show the plot
plt.show()