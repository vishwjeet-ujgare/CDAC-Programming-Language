def display_start_instruction():
    print("\n Welcome to Our tuple Store !!! ")
    print("Please enter a tuple Comma seperated that you would want to perform Operation Upon")
    print("for ex: Pratiksha,Kevin,Sachin,Yuvraj,Sania")
    print("=============================================")

def display_menu():
    print("\n*************** Menu **********************")
    print("Operations supported by our program are :")
    print("  1:  Display all elements of the tuple")
    print("  2:  Display third, fourth and fifth element from the collection ")
    print("  3:  Retrieve element at a given subscript")
    print("  4:  Retrieve elements from a given subscript and to a given subscript")
    print( " 5:	 Find minimum element in the tuple " )
    print( " 6:	 Reverse elements in the tuple " )
    print("  7: Exit the Program ")
    print("\n******************************************") 
 

def tuple_display_members(members) :
    print("Yout Tuple is : ",members)
	

def display_3_4_5_element(members) :
    print("3 to 5 elements are : ",members[2:5])
	

def tuple_retrieve_element(members):
    user_element=input("Enter index of element that you you want to retrive : ")
    try:
        i=int(user_element)
        print("Element at index ",i," is " ,members[i])
        return 
    except ValueError:
    
        pass
        
    print("Please enter only iteger value...")
   
   
	

def tuple_retrieve_elements(members) :
    try:
        start=int(input("Enter Starting index : "))
        end=int(input("Enter Ending  index : "))
        
        if(len(members)<end):
            print("Tuple has only ",end," elements.")
            return
        else:
            if(start==0):
                if input("Do you want to print from 1 element  y/n :").lower()=='y':
                    print(f"Elements from {start+1} to {end} : ",members[start:end])
                    return
               
        print(f"Elements from {start} to {end} : ",members[start:end])
    except ValueError:
        print("Please enter only integer values ...")
        pass
    
	

def find_min_element(members) :
    print("Minimum element in tuple is : ",min(members))
	

def reverse_tuple(members):
    print("reverse tuple :",members[::-1])
