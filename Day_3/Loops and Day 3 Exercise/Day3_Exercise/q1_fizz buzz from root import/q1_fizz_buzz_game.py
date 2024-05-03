# Problem 1 
# ***********************************************************
#  Create a game for FIZZ BUZ and keeping playing with the user untill the user chooses to skip the game
# Add the parent directory of Day_2 to the Python search path
import sys
import os

# Add the parent directory of Day2 to the Python search path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..','..'))
sys.path.append(parent_dir)

# Import the check_Fizz_Buzz function
from Day_2.Conditional_Statements.FizzBizz.my_function_for_fizz_buzz import check_Fizz_Buzz

while True:
    num = int(input("Enter a number: "))
    result = check_Fizz_Buzz(num)
    print(result)

    if input("Do you want to continue (y/n)? ").lower() != 'y':
        break