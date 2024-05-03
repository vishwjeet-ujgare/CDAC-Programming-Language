def calculate_operations(a, b):
    print("     1). You have entered a = ", a, ", b = ", b)

    print("     2). Addition of ", a, " and ", b, " is ", calculate_sum(a,b))

    print("     3). Square of ", a, " is ", calculate_first_num_square(a))

    print("     4).", a, " Raised to ", b, " is ", first_name_raised_to_second(a,b))


def calculate_sum(first_num, second_num):
    return first_num+second_num
    
def calculate_first_num_square( first_num):
    return first_num*2
    
def first_name_raised_to_second( first_num, second_num):
    return first_num**second_num

first_num = int(input("Enter First Number : "))
second_num = int(input("Enter Second Number : "))

# calculate_first_num_square(first_num)
# first_name_raised_to_second(first_num, second_num)

calculate_operations(first_num, second_num)