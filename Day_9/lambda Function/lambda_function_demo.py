# function definition(regular way)
def my_addition(first_num,second_num):
    """receives two numbers from the invoking application and returns addition """
    return first_num+ second_num

# lambda function
# lambda inputparam : return_expression
my_lamdba_add_func = lambda first_num,second_num :  first_num+ second_num

# invoking lambda function
print(my_lamdba_add_func(1,2))

# definitions 
def my_square(first_num):
    """receives two numbers from the invoking application and returns first number squared 2 """
    return str(first_num**2)

my_lambda_square_func = lambda first_num : str(first_num**2)

# invocation
print(my_square(5))
print(my_lambda_square_func(5))


"""
-----------------------------------------------------------------------
EXERCISE on lambda
-----------------------------------------------------------------------
1)  Convert following functions from function_definitions.py into lambda 
    and call them 
"""        

    

