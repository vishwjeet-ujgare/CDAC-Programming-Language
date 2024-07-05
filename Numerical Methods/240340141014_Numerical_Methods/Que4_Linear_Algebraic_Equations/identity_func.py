import matplotlib.pyplot as plt

def f(x):
    return 3*x

#intialize the empty list 
x_new = []
y_new = []

#loop for the range
for x in range (-50,50):
    y = 3*x
    x_new.append(x)
    y_new.append(y)
    
#create the plot
plt.plot(x_new,y_new)

#Add the titles
plt.title('Graph for the equation y = 3*x')
plt.xlabel('x')
plt.ylabel('y')

#show the plot
plt.show()
