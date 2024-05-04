# 4)Create the following program named "my_exception_store" with the menu below :

# Welcome User , What would you like to do today ?
#     1) Create a postive numbered list 
#     Note : raise an exception if the users inserts a negative number OR user creates an empty list 
#     2) Create a negative  numbered list 
#     Note : raise an exception if the users inserts a positive number/Zero OR user creates an empty list
#     3) Create a heterogenous list 
#     Note : raise an exception if the users creates a homogenous list (all elements of same datatype)

#     4) Refresh the program to start with blank lists
#     5) Exit

# Handle exceptions in the script for all operations 
# and let the user continue till he chooses to exit from the program 

# reference code :

class My_Positive_Nume_Exception(Exception):
    print("Enter number is not a Positive")

class My_Negative_Nume_Exception(Exception):
    print("Enter number is not a Negative")
    
def my_exception_store(): 
    my_int_list1=[]
    my_int_list2=[]
    my_het_list3=[]

def start_menu():
    
    print("\n\n-------------------------------------")
    print("Following operations are supported :")
    print("1) Create a positive numbered list  ")
    print("2) Create a negative numbered list  ")
    print("3) Exit  ")
    print("\n\n-------------------------------------") 


def create_positive_numbered_list():
    print("Enter positive element one by one to exist enter ee")
    l=[]
    
    while(True):
        element=input("Enter Your Element : ")
        
        if(element =="ee"):
            print(l)
            break
        
        try:
            e=int(element)
            if(e>0):
                l.append(e)
            else:
                raise My_Positive_Nume_Exception
        except Exception:
            print("Please enter numbers  only")
            

    
def create_negative_numbered_list():
    print("Enter Negative element one by one to exist enter ee")
    l=[]
    
    while(True):
        element=input("Enter Your Element : ")
        
        if(element =="ee"):
            print(l)
            break
        
        try:
            e=int(element)
            
            if(e<0):
                l.append(e)
            else:
                raise My_Negative_Nume_Exception
        except Exception:
            print("Please enter numbers  only")
            pass  
         
while(True):
    try:

        start_menu()
    
        choice = int(input("Please enter your choice : "))
    
        if choice ==1:
            create_positive_numbered_list()
            
        elif choice ==2:
            create_negative_numbered_list()
             
        elif choice ==3:
            break
        else:
            print("Please choose something from the above")
    except:
       pass
            
  
