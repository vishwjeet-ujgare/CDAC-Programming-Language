import matplotlib.pyplot as plt
def f(C):
    return C

#set the value of c
C = 3

#intialize th empty list
x_new = []
y_new = []

#loop for the range
for x in range(-50,50):
    y = C
    x_new.append(x)
    y_new.append(y)

#Create the graph
plt.plot(x_new, y_new)

#add the title
plt.title('Graph of given function is y = C')
plt.xlabel('x')
plt.ylabel('y')

# show the graph\
plt.show()