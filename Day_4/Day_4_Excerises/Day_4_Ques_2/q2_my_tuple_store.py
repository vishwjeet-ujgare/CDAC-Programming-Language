# 1.2) Create a program named "my_tuple_store"
# Sample code template for My tuple store starts

from q2_my_tuple_store_my_functinality import *
	
  
def my_tuple_store():
    display_start_instruction()
    
    members = tuple(input('Enter Here : ').split(","))

    while(True):
        display_menu()
        
        choice = int(input("Please enter your choice "))
        
        if choice   ==1:
            tuple_display_members(members) 
        elif choice ==2:
            display_3_4_5_element(members) 
        elif choice ==3:
            tuple_retrieve_element(members)
        elif choice ==4:
            tuple_retrieve_elements(members) 
        elif choice ==5:
            find_min_element(members) 
        elif choice ==6:
            reverse_tuple(members) 
        elif choice ==7:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")

my_tuple_store()		
# Sample code template for My tuple store ends	