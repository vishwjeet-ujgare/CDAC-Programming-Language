# Sample code template for my set store

def start_menu():
    print("\n*************** Menu **********************")
    print("Operations supported by our program are :")
    print("	1: Union")
    print("	2: Intersection ")
    print("	3: A-B")
    print("	4: B-A")
    print("	5: Take a element from user and Display if that element is a member of set B ")
    print("	6: Display number of elements in the set A")
    print(" 7: Display number of elements in the set B")
    print("	8: Add an element taken from the user to the set A")
    print("	9: Add multiple elements taken from the user to the set A")
    print("	10: Remove an element taken from the user from set A")
    print(" 11: Exit")


def set_union(first_set,second_set):
  set_display(first_set)
  set_display(second_set)
  print("Union",first_set.union(second_set))

def set_intersection(first_set,second_set):
  set_display(first_set)
  set_display(second_set)
  print("Intersection",first_set.intersection(second_set))  

def set_minus(first_set,second_set):
  set_display(first_set)
  set_display(second_set)
  print("Difference",first_set.difference(second_set))      

def is_member_of_set(rcv_set , is_str = True):
    element= input("Please enter element to search for ") 
    if not is_str :
        element= int(element )

    print(f"Element: {element} is present(True/False): { element in rcv_set }")  
    set_display(rcv_set)

def set_count(rcv_set):
   print(len(rcv_set))
   
def set_display(rcv_set):
   print(rcv_set)

def set_add_element(rcv_set , is_str = True):
    element= input("Please enter element to search for ") 
    if not is_str :
        element= int(element )
    rcv_set.add(element)
    set_display(rcv_set)
	
def set_add_elements(rcv_set, is_str = True):
    if is_str:
        rcv_set.update(set(input("Please enter comma seperated elements for the set ").split(",")))   
    else:
        temp_set = set()
        for i in range(int(input("element count:"))):
            temp_set.add(int(input("element")))
        rcv_set.update(temp_set)    
    set_display(rcv_set)
	
def set_remove_element(rcv_set, is_str = True):
    element= input("Please enter element to search for ") 
    if not is_str :
        element= int(element )
    
    rcv_set.discard(element)
    set_display(rcv_set)            

def my_set_store():
    print("\n Welcome to Our Set Store !!! ")
    #    # set of strings
    is_str = True
    setA = set(input("Please enter comma seperated elements for the set A").split(","))
    setB = set(input("Please enter comma seperated elements for the set B").split(","))

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

