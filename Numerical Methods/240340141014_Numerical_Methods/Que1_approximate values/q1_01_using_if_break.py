
# 1) Write a python program to calculate approximate values of cube root of 27. Avoid infinite looping using below all three method
# • Write a code using if-break statement


guess = 0.0
cube = 27
increment = 0.0001

# #3 write a code using for loop on a guess value
guess = 0.0
cube = 27
increment = 0.5
epison = 0.01

for i in range(100):
    guess += increment
    if abs(guess**3 - cube) < epison:
        print(guess, "is close enought to cube root of", cube)
        break

else:
    print(guess, "is not close enought to cube root of", cube)
