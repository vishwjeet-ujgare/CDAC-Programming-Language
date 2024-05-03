
"""
Exercise 2 : Create a dictionary like this by taking values from the user:
here the idea is to support a generic dictionary where the values could be of any datatype
and the keys are strings
"""

# Solution:

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