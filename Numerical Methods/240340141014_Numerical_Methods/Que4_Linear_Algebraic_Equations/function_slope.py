#write a python code for function  f(x) = x + C for plotting the slope

import matplotlib.pyplot as plt
def f(x,C):
    return x+ C

#Set the value of C
C = 3

#initalize the empty list
x_new = []
y_new = []

#Loop for the range is 
for x in range(-100 , 100):
    y = x + C
    x_new.append(x)
    y_new.append(y)
    
#Create the plot
plt.plot(x_new, y_new)

#Add the titles
plt.title('Graph of the  equaton y = x + C')
plt.xlabel('x')
plt.ylabel('y')

#show the plot
plt.show()
    