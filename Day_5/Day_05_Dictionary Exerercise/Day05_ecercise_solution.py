

def dict_display_capitals(capitals):
    """Display number of elements in the capitals collection"""
    print(f"capitals dictionary = {capitals}")

def dict_add_element(capitals):
    """Add "Afghanistan": "Kabul"  to the capitals collection """
    inp_key = input("Please enter the key to add ")
    inp_val = input("Please enter the value to add ")
    capitals[inp_key]= inp_val
    dict_display_capitals(capitals)		

def dict_add_elements(capitals):
    """Add Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella to the capitals collection"""    
    sub_dict_of_capitals= {}
    keys = input("Please enter the additional countries as keys for ex : India,USA,Srilanka").split(',')
    for elem in keys :
        sub_dict_of_capitals[elem] = input(f"Please enter the capital for {elem}: ").strip()
    capitals.update(sub_dict_of_capitals)    
    dict_display_capitals(capitals)		
	
def dict_remove_element(capitals):
    """Remove the USA from the collection"""    
    capitals.pop(input("Please enter the key you would want to remove"))
    dict_display_capitals(capitals)

def dict_show_value_for_a_key(capitals):
    print(f'The value for the key : {capitals.get(input("Please enter the key you would like to lookup for "),"Not Found")} ')
    dict_display_capitals(capitals)		

def dict_update_or_add_a_key(capitals):
    input_key = input("Please enter the key that you want want to add or update") 	
    input_value = input("Please enter the value that you want want to add or update")	
    capitals[input_key] = input_value
    dict_display_capitals(capitals)		

def my_dict_store():
    print("\n Welcome to Our Dict Store !!! ")

    capitals= {}
    keys = input("Please enter the countries as keys for ex : India,USA,Srilanka").split(',')
    for elem in keys :
        capitals[elem] = input(f"Please enter the capital for {elem}: ").strip()

    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("    1: Display elements in the capitals collection")
        print('    2: Add an element to the capitals collection like --> Afghanistan: Kabul')
        print('    3: Add multiple elements to the capitals collection like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella')
        print("    4: Remove an element from the collection 	")
        print("    5: Take a key from the user and show value if it is present in the dictionary")
        print("    6: Take a key from the user update it if it is present in the dictionary or add the key to the dictionary")
        print("    7: Exit the Program ")
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

my_dict_store()

# """
# Exercise 2 : Create a dictionary like this by taking values from the user:
# here the idea is to support a generic dictionary where the values could be of any datatype
# and the keys are strings
# """
# # Solution:

def menu(elem):
    print(f'Please choose a datatype for the {elem} from below')
    print('1: Integer')
    print('2: Float')
    print('3: String')
    print('4: Tuple')
    print('5: List')
    print('6: Dictionary')
    print('7: Set')
    print('8: Frozenset')
    
    dt= int(input())
    if dt != 6 :
        raw_string = input(f"Please enter value for {elem}")
    if dt ==1 :
        return int(raw_string)
    elif dt ==2 :
        return float(raw_string)
    elif dt ==3 :
        return raw_string
    elif dt ==4 :
        return tuple(raw_string.split(','))
    elif dt ==5 :
        return raw_string.split(',')
    elif dt ==6 :
        d = {}
        keys = []
        for i in range(int(input('How many keys'))):
            keys.append(input("Key_name"))
        for elem in keys :
            d[elem] = menu(elem)    
        return d     
    elif dt ==7 :
        return set(raw_string.split(','))
    elif dt ==8 :
        return frozenset(raw_string.split(','))


d = {}
keys = ['employee_id','employee_name','account_number','salary','address']
# keys = ['employee_id','address']
for elem in keys :
    d[elem] = menu(elem)

print(d)  