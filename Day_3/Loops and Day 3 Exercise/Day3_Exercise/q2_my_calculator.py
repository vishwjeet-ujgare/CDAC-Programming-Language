''' 
Addition/Squaring/exponenation should be done as part of single function named 
"my_calculator"
which takes in type of operation, number1,number2 as input 
and outputs the answer based on the operation
We need to keep executing my_calculator function 
untill user choose to skip the application
'''

# Import the my_addition, my_square, and my_exponenation functions from the function_definitions module
from q2_calculator_funtionality import my_addition, my_square, my_exponenation

def my_calculator():
    """
    Display a menu of available operations and prompt the user to select one.
    Based on the user's selection, perform the corresponding operation on the input numbers.
    """
    print("****************** MENU ************************")
    print("1: Addition")
    print("2: Square")
    print("3: Exponentation ")

    choice = int(input("Please select your choice : "))

    if choice == 1:
        """
        Perform addition on the input numbers and print the result.
        """
        first_num = int(input("Please enter First number : "))
        second_num = int(input("Please enter Second number : "))
        returned_value = my_addition(first_num, second_num)
        print("The Addition of the numbers is ", returned_value)

    elif choice == 2:
        """
        Perform squaring on the input number and print the result.
        """
        first_num = int(input("Please enter First number : "))
        returned_value = my_square(first_num)
        print("The Square of the number is ", returned_value)

    elif choice == 3:
        """
        Perform exponentation on the input numbers and print the result.
        """
        first_num = int(input("Please enter First number : "))
        second_num = int(input("Please enter Second number : "))
        returned_value = my_exponenation(first_num, second_num)
        print("The exponenation of the numbers is ", returned_value)

def iterative_calculator():
    """
    Run the my_calculator function in an infinite loop until the user decides to stop.
    """
    while True:
        my_calculator()
        if input("\n Do you want to continue (Y/N)").lower() == 'n':
            break

# Call the iterative_calculator function to start the application
iterative_calculator()