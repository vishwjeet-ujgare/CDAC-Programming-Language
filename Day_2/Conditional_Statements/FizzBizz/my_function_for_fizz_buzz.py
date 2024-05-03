def check_Fizz_Buzz(num):
    if(num%3==0 and num%5==0 ):
        return "Fizz Buzz"
    elif (num % 5==0):
        return "Buzz"
    elif (num%3==0):
        return "Fizz "
    else:
        return "Invalid Input"
