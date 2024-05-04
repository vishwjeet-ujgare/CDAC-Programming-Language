# Q3 Create a program named "my_set_store" which support following operations on two sets
#     provided by user 

# for ex: 
# 	A = {1,2,3,4,5}
# 	B = {18,19,20,21}
# is provided by the user

# Operations supported by our program are :
# 	1: Union
# 	2: Intersection 
# 	3: A-B
# 	4: B-A
# 	5: Take a element from user and Display if that element is a member of set B 
# 	6: Display number of elements in the set A
#     7: Display number of elements in the set B
# 	8: Add an element taken from the user to the set A
# 	9: Add multiple elements taken from the user to the set A
# 	10: Remove an element taken from the user from set A

from q3_my_set_store_functionality import *



# setA= set(input("Please enter comma seperated elements for the set A").split(","))
# setB= set(input("Please enter comma seperated elements for the set B").split(","))
setA={1,2,3,4,5,6}
setB={2,4,6,8,10}


# #In case you need a set of numbers you may want to do below instead of above two lines
# is_str = False

# f_set = set(input("input set A comma seperated").split(','))
# setA = set()
# for elem in f_set:
#     setA.add(int(elem))
    
# f_set = set(input("input set B comma seperated").split(','))
# setB = set()
# for elem in f_set:
#     setB.add(int(elem))
    
while(True):
    start_menu()
    choice = int(input("Please enter your choice "))

    if choice   ==1:
        set_union(setA,setB) 
    elif choice ==2:
        set_intersection(setA,setB)
    elif choice ==3:
        set_minus(setA,setB)
    elif choice ==4:
        set_minus(setB,setA)
    elif choice ==5:
        is_member_of_set(setB) 
    elif choice ==6:
        set_display(setA)
    elif choice ==7:
        set_display(setB)
    elif choice ==8:
        set_add_element(setA)
    elif choice ==9:
        set_add_elements(setA)
    elif choice ==10:
        set_remove_element(setA)
    elif choice ==11:
        break
    else:
        print("Invalid Input , Please Try Again !!!!  ")  
			
		
