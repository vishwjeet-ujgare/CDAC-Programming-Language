'''Create a program named "my_dict_store" which support following operations on 
dictionary named "capitals" which would have keys as their country and values as their capitals
respectively from the user
for ex: "India" : "New Delhi" ,"USA" : "Washington DC","Nepal": "Kathmandu","Ukraine" : "Kyiv"
is provided by the user 

Operations supported by our program are :
    1: Display number of elements in the capitals collection
    2: Add an element to the capitals collection like --> Afghanistan: Kabul
    3: Add multiple elements to the capitals collection like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella
    4: Remove an element from the collection 	
    5: Take a key from the user and show value if it is present in the dictionary
    6: Take a key from the user update it if it is present in the dictionary or add the key to the dictionary 	


Keep asking the user for the operation in this store untill he chooses to exit from the program
'''
from q1_my_dict_store_functinality import *



capitals={}

my_dict_store()

takeDecFromUser(capitals)

dict_display_capitals(capitals) 
 

while(True):
  
    startMenu()
    choice = int(input("Please enter your choice "))
    
    if choice   ==1:
        dict_display_capitals(capitals) 
        
    elif choice ==2:
        dict_add_element(capitals)
    
    elif choice ==3:
        dict_add_elements(capitals)
    
    elif choice ==4:
        dict_remove_element(capitals) 
    
    elif choice ==5:
        dict_show_value_for_a_key(capitals)
    
    elif choice ==6:
        dict_update_or_add_a_key(capitals)
    
    elif choice ==7:
        break
    
    else:
        print("Invalid Input , Please Try Again !!!!  ")




