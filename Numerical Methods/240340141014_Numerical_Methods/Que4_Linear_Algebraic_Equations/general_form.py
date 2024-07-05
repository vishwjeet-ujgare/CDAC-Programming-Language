import matplotlib.pyplot as plt

#intialize the empty list
x_new = []
y_new = []

#loop for thge range
for x in range(-50 , 50):
    y = 6 - 2*x / 3
    x_new.append(x)
    y_new.append(y)
    
#create the plot
plt.plot(x_new, y_new)

#Add the title
plt.title('Graph for y = 6 - 2*x /3')
plt.xlabel('x')
plt.ylabel('y')

#show the plot
plt.show()