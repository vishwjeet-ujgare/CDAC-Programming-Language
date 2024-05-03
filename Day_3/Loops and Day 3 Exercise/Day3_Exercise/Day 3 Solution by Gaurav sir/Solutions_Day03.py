"""Create a game for FIZZ BUZ and keeping playing with the user untill the user chooses to skip the game"""
def fizz_buzz():
        
    num = int(input("Please enter the number"))

    if num %5==0 and num % 3 ==0 :
        print("Fizz Buzz")
    elif num%3 == 0 :
        print("Fizz")
    elif num%5 == 0 :
        print("Buzz")
    else:
        print("Invalid Input")

def play_game():
    while(True):
        fizz_buzz()	
        if input("\n Do you want to continue (Y/N)").lower() == 'n':
            break

# function calls
play_game()  

"""
Addition/Squaring/exponenation should be done as part of single function named 
"my_calculator"
which takes in type of operation, number1,number2 as input 
and outputs the answer based on the operation
We need to keep executing my_calculator function 
untill user choose to skip the application
"""

from function_definitions import my_addition,my_exponenation,my_square
def my_calculator():
    print("****************** MENU ************************")
    print("1: Addition")
    print("2: Square")
    print("3: Exponentation ")
    choice = int(input ("Please select your choice"))

    if choice == 1 :
        first_num = int(input("Please enter First number:"))
        second_num = int(input("Please enter Second number:"))
        returned_value = my_addition(first_num,second_num)
        print("The Addition of the numbers is ",returned_value)

    elif choice == 2 :
        first_num = int(input("Please enter First number:"))
        returned_value = my_square(first_num)
        print("The Square of the number is ",returned_value)
    elif choice == 3 :
        first_num = int(input("Please enter First number:"))
        second_num = int(input("Please enter Second number:"))
        returned_value = my_exponenation(first_num,second_num)
        print("The exponenation of the numbers is ",returned_value)

def iterative_calculator():
    while(True):
        my_calculator()	
        if  input("\n Do you want to continue (Y/N)").lower() == 'n':
            break

iterative_calculator()  



# """3) Take a number from the user and print all Odd numbers from 1 to that number """

number_from_user = int(input("Please enter a number "))

current_number_being_checked = 1
while(current_number_being_checked<= number_from_user):
    if current_number_being_checked%2 !=0:
        print(current_number_being_checked,end=" ")
    current_number_being_checked+=1

# or 
current_number_being_checked = 1
while(current_number_being_checked<= number_from_user):
    print(current_number_being_checked,end=" ")
    current_number_being_checked+=2
    
# using for loop
for i in range(1,number_from_user+1,2):
    print(i , end = " ")

"""4) Take a number from the user and print all Even numbers from 1 to that number """

number_from_user = int(input("Please enter a number "))

current_number_being_checked = 0
while(current_number_being_checked<= number_from_user):
    if current_number_being_checked%2 ==0:
        print(current_number_being_checked,end=" ")
    current_number_being_checked+=1


# or 
current_number_being_checked = 0
while(current_number_being_checked<= number_from_user):
    print(current_number_being_checked,end=" ")
    current_number_being_checked+=2
    
# using for loop
for i in range(0,number_from_user+1,2):
    print(i , end = " ")   
