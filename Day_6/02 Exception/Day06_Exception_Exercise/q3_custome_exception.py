# 3) Create program that takes age of the user as input 
# and prints number of days that user has lived for 
# Exception handle the code such that if the user has lived for more than 
# 100001 days then user should get the message
# , you lived for so long , may be you will die soon:)



class My_Exception(Exception):
    pass

try:
    age= int(input("Enter you age : "))

    if(age >100001):
        raise My_Exception
    else:
        print(f"You have lived for {age} days")
except My_Exception:
    print(f"You lived for so long {age} days , may you will die soon :)")