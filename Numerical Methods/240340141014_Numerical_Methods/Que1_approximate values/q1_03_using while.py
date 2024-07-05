# 1) Write a python program to calculate approximate values of cube root of 27. Avoid infinite looping using below all three method
# • Write a code using For Loop on a guess value.

guess = 0.0
cube = 27
increment = 0.0001


while abs(guess**3 - cube) > increment:
    guess += increment
print(f"The cube root of{cube} is {guess :.4f}\n")