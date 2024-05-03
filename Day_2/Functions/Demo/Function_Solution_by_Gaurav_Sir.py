def my_addition(first_num,second_num):
    """
    1) receives two numbers from the invoking application and returns 
        a) addition 
    """
    return first_num+ second_num


def my_square(first_num):
    """
    1) receives two numbers from the invoking application and returns 
        b) first number squared 2 
    """
    return first_num**2

def my_exponenation(first_num,second_num):
    """
    1) receives two numbers from the invoking application and returns 
        c) first number raised to number second number
    """
    return first_num**second_num


def my_uppercase_func(received_string):
    """
    # 2) receives String and returns upper case of the input string
    """
    return received_string.upper()


def raise_sal_percent(existing_salary,raise_salary_percentage):
    """
    3) receives "raise_salary_percentage" , salary raise ,
    percentage from the user, 
    returns the incremented salary to the console
    """
    return existing_salary + (existing_salary*raise_salary_percentage/100) 
    
def get_height(height):
    """
    4) receives height from the user in cms and returns the user height back 
    in foot/feet and inches
    """
    return round((height/30.48),2)
    

def convert_to_rupee(no_of_dollars):
    """
    5) receive no of the dollars from the user apply the conversion of 
    1 dollar = 82 rupees and return the amount to the console in rupees
    """
    return no_of_dollars*82

def get_fare_details(source, destination, fare_in_INR, discount_rate_percentage):
    """
    6) receive source, destination, fare in INR, discount_rate percentage from the user and return the 
    string ex: "Fare from mumbai to pune is 400 INR after applied discount of 5% it is 380 INR"
    """
    return "Fare from " + source +" to " + destination + " is " + str(fare_in_INR)  + " INR after applied discount of " + str(discount_rate_percentage)+ f"% it is "+ str(fare_in_INR- (fare_in_INR*discount_rate_percentage/100))  


# invocations
first_num = int(input("Please enter First number:"))
second_num = int(input("Please enter Second number:"))
returned_value = my_addition(first_num,second_num)
print("The Addition of the numbers is ",returned_value)

returned_value = my_square(first_num)
print("The Square of the number is ",returned_value)

returned_value = my_exponenation(first_num,second_num)
print("The exponenation of the numbers is ",returned_value)

my_string = input("Please enter a String: ")
returned_value = my_uppercase_func(my_string)
print("Upper case of the string is ",returned_value)

existing_salary = int(input("Pleased enter the existing_salary"))
raise_salary_percentage = int(input("Pleased enter the percentage"))

returned_value= raise_sal_percent(existing_salary,raise_salary_percentage)
print("The incremented salary is ",returned_value)

height = int(input("Pleased enter height in cms "))
returned_value= get_height(height)
print("Height in feet is ",returned_value)

no_of_dollars = int(input("Pleased enter no of dollars "))
returned_value= convert_to_rupee(no_of_dollars)
print("Amount is INR is " ,returned_value)

source = input("Pleased enter the source ")
destination = input("Pleased enter the destination ")
fare = float(input("Pleased enter the fare "))
discount_rate = float(input("Pleased enter the discount_rate in percentage "))

returned_value=get_fare_details(source, destination, fare, discount_rate)
print(returned_value)