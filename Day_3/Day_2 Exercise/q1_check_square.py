from day2_exercise_functionality import *


# 1) Take values of length and breadth of a rectangle from user and check if it is square or not.

l=float(input("Enter length : "))
b=float(input("Enter length : "))

if(isSquare(l,b)):
    print(f"with value of l={l} and b={b} it is SQUARE")
else:
    print(f"with value of l={l} and b={b} it is NOT A SQUARE")
    

