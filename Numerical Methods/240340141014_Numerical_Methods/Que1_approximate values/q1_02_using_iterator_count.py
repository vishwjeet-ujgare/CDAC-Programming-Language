
# 1) Write a python program to calculate approximate values of cube root of 27. Avoid infinite looping using below all three method
# • Write a code using iteration counter


guess = 0.0
cube = 27
increment = 0.0001


#2 write a code using iteration counter
cube = 27
epison = 0.00001
guess = cube / 2.0
iteration_counter = 0 

while True:
    iteration_counter+=1
    guess_new = (2*guess + cube / (guess **2)) / 3.0
    if abs(guess_new - guess) < epison:
        break
    guess = guess_new
    
print(f"iteration counter: {iteration_counter}")