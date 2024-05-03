# 1.1) Create a program named "my_list_store"
# which support following operations on list named "members" which is provided by the user 
# for ex: Pratiksha,Kevin,Sachin,Yuvraj,Sania is provided by the user 

# Operations supported by our program are :
#   1:  Display all the elements in the members list
#   2:  Add an element to the members collection like 'Sehwag' 
#   3:  Add elements to the members collection like ['David','Bret','Sanju']
#   4:  Remove a member from the collection at a given subscript
#   5:  Remove the last member from the collection 
#   6:  Display third, fourth and fifth element from the collection 

# Keep asking the user for the operation in this store untill he chooses to exit from the program

# Sample code template for my_list_store starts
from q1_my_list_store_functionality import *
    	  
    
def my_list_store():
    display_start_instructions()
  
    # members = input("Enter Your List Here :").split(",")
    members=["Pratiksha","Kevin","Sachin","Yuvraj","Sania"]
    
    print("=============================================")
    
    while(True):
        display_menu()
        
        choice = int(input("Please enter your choice :"))
        
        if choice==1:
            list_display_members(members) 
        elif choice ==2:
            members=list_add_element(members) 
            display_list_members_with_msg(members,"New List : ")
        elif choice ==3:
            members=list_add_elements(members)
            display_list_members_with_msg(members,"After Adding Elements : ")
        elif choice ==4:
            members=list_remove_element(members)
        elif choice ==5:
            remove_last_element(members) 
        elif choice ==6:
            display_3_4_5_element(members)
            
        elif choice ==7:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")

my_list_store()		