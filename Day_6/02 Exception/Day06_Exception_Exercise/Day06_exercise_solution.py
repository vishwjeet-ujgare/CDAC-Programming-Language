
# solutions

"""
1) Write a program that creates a dictionary like this 
{
    1: "red" , 2: "Blue" , 3: "Orange"
}
Now take the key as input from the user and print its corresponding colour 
(Exception handle the code to terminate gracefully by printing 
Colour not found if the key doesnot exists )
# """
# try:
#     d= {1: "red" , 2: "Blue" , 3: "Orange"}
#     print(d[int(input("Please enter the key for which you need to search for the colour"))])
# except KeyError:
#     print("key does not exists ")
    
"""
2) Write a program that creates a list of 5 elements of your choice 
Now take the index that the user want the data of and print the value at that 
location 
Exception handle the code to  terminate gracefully by printing 
Value not found if the index doesnot exists 
"""
# try:
#     l= [1,2,3,4,5]
#     print(l[int(input("Please enter index location "))])
# except IndexError:
#     print("index does not exists ")


"""
3) Create program that takes age of the user as input 
and prints number of days that user has lived for 
Exception handle the code such that if the user has lived for more than 
100001 days then user should get the message
, you lived for so long , may be you will die soon:)
# """
class My_exception(Exception):
    pass

try:
    inp = int(input("Please enter your age"))*365
    if ( inp > 100001):
        raise My_exception
    else:
        print(f"You have lived for {inp} days ")
except My_exception:
    print(f"you lived for so long {inp} days , may be you will die soon:)")


# my custom exception created 
class negative_number_error(Exception):
    pass

def create_positive_numbered_list(my_list):
    """
    1) Create a postive numbered list 
    Note : raise an exception if the users inserts a negative number OR user creates an empty list 
    """
    for cntr in range(0,int(input("Please enter number of elements to the positive numbered list"))):
        num = int(input("Please enter a number to be added ")) 
        if (num ) <0:
            raise  negative_number_error
        else:
            my_list.append(num)
    print(my_list)   

# my custom exception created 
class positive_number_error(Exception):
    pass

def create_negative_numbered_list(my_list):
    """
    2) Create a negative  numbered list 
    Note : raise an exception if the users inserts a positive number/Zero OR user creates an empty list
    """
    for cntr in range(0,int(input("Please enter number of elements to the negative numbered list"))):
        num = int(input("Please enter a number to be added "))
        if num >0:
            raise  positive_number_error
        else:
            my_list.append(num)
    print(my_list)   
    
# invocation 

def my_exception_store(): 
    my_int_list1=[]
    my_int_list2=[]
    my_het_list3=[]

    while(True):
        try:
            print("Welcome to my_exception_store !!!!")
            print("-------------------------------------")
            print("Following operations are supported :")
            print("1) Create a positive numbered list  ")
            print("2) Create a negative numbered list  ")
            print("3) Refresh the program to start with blank lists")
            print("4) Exit  ")
            
            choice = int(input("Please enter your choice !!!! "))
            if choice ==1:
                create_positive_numbered_list(my_int_list1)
            elif choice ==2:
                create_negative_numbered_list(my_int_list2)
            elif choice ==3:
                my_int_list1.clear()
                my_int_list2.clear()
                my_het_list3.clear()
                print("Store restarted !!!! ")
            elif choice ==4:
                break
            else:
                print("Please choose something from the above")
        except negative_number_error:     
            print("We received a negative number in the list and I handled negative_number_error exception")
            my_int_list1.clear()
        except positive_number_error:     
            print("We received a positive number in the list and I handled positive_number_error exception")
            my_int_list2.clear()
            
my_exception_store()    

