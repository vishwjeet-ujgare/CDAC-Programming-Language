import math
x=0.1


for i in range(1, 25):
    f = math.cos(x)
    error = x-f

    if abs(error) <= 0.001:
        break
    else:
        x =f 
    print("Value of x and cos(x): ", x)
    
print("Value of : ",error)

		
	