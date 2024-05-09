
                # # definitions 
                # def my_square(first_num):
                #     """receives two numbers from the invoking application and returns first number squared 2 """
                #     return str(first_num**2)

                # my_lambda_square_func = lambda first_num : str(first_num**2)

                # # invocation
                # print(my_square(5))
                # print(my_lambda_square_func(5))

# ==========================================

# def my_addition(first_num,second_num):
#     """
#     1) receives two numbers from the invoking application and returns 
#         a) addition 
#     """
#     return first_num+ second_num


# def my_square(first_num):
#     """
#     1) receives two numbers from the invoking application and returns 
#         b) first number squared 2 
#     """
#     return first_num**2


# def my_exponenation(first_num,second_num):
#     """
#     1) receives two numbers from the invoking application and returns 
#         c) first number raised to number second number
#     """
#     return first_num**second_num


# def my_uppercase_func(received_string):
#     """
#     # 2) receives String and returns upper case of the input string
#     """
#     return received_string.upper()



# def raise_sal_percent(existing_salary,raise_salary_percentage):
#     """
#     3) receives "raise_salary_percentage" , salary raise ,
#     percentage from the user, 
#     returns the incremented salary to the console
#     """
#     return existing_salary + (existing_salary*raise_salary_percentage/100) 
    
# def get_height(height):
#     """
#     4) receives height from the user in cms and returns the user height back 
#     in foot/feet and inches
#     """
#     return round((height/30.48),2)
    

# def convert_to_rupee(no_of_dollars):
#     """
#     5) receive no of the dollars from the user apply the conversion of 
#     1 dollar = 82 rupees and return the amount to the console in rupees
#     """
#     return no_of_dollars*82

# def get_fare_details(source, destination, fare_in_INR, discount_rate_percentage):
#     """
#     6) receive source, destination, fare in INR, discount_rate percentage from the user and return the 
#     string ex: "Fare from mumbai to pune is 400 INR after applied discount of 5% it is 380 INR"
#     """
#     return "Fare from " + source +" to " + destination + " is " + str(fare_in_INR)  + " INR after applied discount of " + str(discount_rate_percentage)+ f"% it is "+ str(fare_in_INR- (fare_in_INR*discount_rate_percentage/100))  

"""
-----------------------------------------------------------------------
EXERCISE on lambda
-----------------------------------------------------------------------
1)  Convert Above functions from function_definitions.py into lambda 
    and call them 
"""        


my_addition_lambda=lambda first_num,second_num : first_num+second_num

my_square_lambda=lambda first_num : (first_num**2)

my_exponenation_lambda=lambda first_num, second_num : first_num**second_num

my_uppercase_func_lambda=lambda recevied_string:recevied_string.upper()

raise_sal_percent_lambda=lambda existing_salary,raise_salary_percentage:(existing_salary+(existing_salary*raise_salary_percentage/100))

get_height_lambda=lambda height : round((height/30.48),2)

convert_to_rupee_lambda=lambda no_of_dollars:no_of_dollars*82

# get_fare_details_lambda=lambda source, destination, fare_in_INR, discount_rate_percentage:("Fare from " + source +" to " + destination + " is " + str(fare_in_INR)  + " INR after applied discount of " + str(discount_rate_percentage)+ f"% it is "+ str(fare_in_INR- (fare_in_INR*discount_rate_percentage/100)) )


print("==========================================")
print("Additiong : ",my_addition_lambda(5,7))
print("Square : ",my_square_lambda(5))
print("Exponention : ",my_exponenation_lambda(2,2))
print("convert into upper case : ",my_uppercase_func_lambda("vishwjeet"))
print("Riase salray : ",raise_sal_percent_lambda(100,10))
print("Convert Ruppes to lambda : ",convert_to_rupee_lambda(1))
