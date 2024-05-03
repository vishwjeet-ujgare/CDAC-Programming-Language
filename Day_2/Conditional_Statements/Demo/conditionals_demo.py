"""
# only if 
if condition1 :
   executes when the condition1 is true

# if else 
if condition1 :
   executes when the condition1 is true
else :
   executes when the condition1 is false
   
#if elif else ladder   
if condition1 :
   executes when the condition1 is true
elif condition2 :
   executes when the condition2 is true and condition1 is false
else :
   executes when the both condition1 and condition2 is false

"""  
# demo

"""
 hot -> cold coffee
 cold -> green tea
 raining -> tea
 water
"""
weather = "raining"

# only if 
if weather == "hot":
    print("I am having cold coffee")

# if else
if weather == "hot":
    print("I am having cold coffee")
else:    
    print("I am having water")
    
# if elsif ladder    
if weather == "hot":
    print("I am having cold coffee")
elif weather == "cold":
    print("I am having green tea")
elif weather == "raining":    
    print("I am having tea")
else:    
    print("I am having water")
print("Bye , Visit again!!!")


# nesting the if else if ladder
weather = "cold"
personal_preference = "Hot"
if weather == "Sunny":
	if personal_preference == "Hot":
		print(" I am having  Hot coffee")
	else:
		print(" I am having  cold coffee")	
elif weather == "raining":
	if personal_preference == "Hot":
		print(" I am having  hot tea")
	else:
		print(" I am having  cold tea")
elif weather == "cold":
	if personal_preference == "Hot":
		print(" I am having  hot green tea")
	else:
		print(" I am having  cold green tea")
else:
	if personal_preference == "Hot":
		print(" I am having  hot water")
	else:
		print(" I am having  cold water")
print(" Thank you !")


"""
we will take number from the user 
if the number is divisible by 3 print Fizz    
if the number is divisible by 5 print Buzz
if the number is divisible by 3 and also divisible by 5 print Fizz Buzz

Testcase : 
    21 --> Fizz
    50 --> Buzz
    15 --> Fizz Buzz
    22 --> Invalid Input 
"""

