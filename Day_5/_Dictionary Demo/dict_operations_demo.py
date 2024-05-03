"""
https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

Theory:
------
# general notion around dictionary
# keys are unique and immutable 
{
 key : value,
 key1 : value1,
}



# create a dictionary Different Ways to Create a Python Dictionary
{} //Empty Dictionary

{
	1: "one",
	2: "two"
 }

dict([(1,"one"),(2,"two")])




# SELECT/ RETRIEVE Operation
d = {
	1: "one",
	2: "two"
 }

# single element
d[1] -- key error / d.get(1) 


# multiple element (all)
d.keys() / d --  all keys from the dictionary
d.values() -- all values from the dictionary
d.items() -- all elements from the dictionary



# DELETE Operation

# single element
del d[3]
d.pop(3)
d.popitem() -- from the last (LIFO)




# UPDATE Operations

# ADD  (the key is not present in d)
d[3] = "Three" ( single element) / d.update({3: "Three"})

# multiple elements (the keys from the temp_dictionary are not present in d)
temp_dictionary = {4: "Four" , 5: "Five"}
d |= temp_dictionary 
or 
d.update(temp_dictionary)

# ASSIGN  (the key is present in d)
# single element
d[3] = "New three" / d.update({3: "new Three"})

# multiple element (the keys from the temp_dictionary ARE present in d
temp_dictionary = {3: "new_three" , 1 :"new_one"}
d |= temp_dictionary 
or or 
d.update(temp_dictionary)

"""

## DEMO CRUD Operations on Dictionary 

# # creating a dictionary 
# d = {'name': 'Gaurav' , 'rollno' : 1 ,'rollno' : 2}
# print(d)

# d= dict(name = 'Sagar' , rollno = 2 )
# print(d)

# d= dict([('name','Deepak') ,( 'rollno' , 3 )])
# print(d)

# # adding to a blank dictionary 
# d= {}
# no_of_items = int(input("How many items you want to add"))
# for i in range(0,no_of_items,1):
#     key = input('Please enter the key ')    
#     value = input('Please enter the value ')    
#     d[key] = value # d.update({key:value})

# print(d)

# # adding to a blank dictionary 
# d= {}
# keys = input("Please enter keys comma separated").split(",")
# values= input("Please enter values comma separated").split(",")

# for i in range(0,len(keys)) :
#     d[keys[i]] = values[i]

# print(d)

# ## SELECT/retrieve 
d= {'employee_id': 100, 'address': ['pune', 'nagpur']}

# print("The employee id is " , d['employee_id'])
# print("The employee id1 is " , d['employee_id1']) #KeyError: 'employee_id1'


# print("""
#       get(key[, default])
#         Return the value for key if key is in the dictionary, else default.
#         If default is not given, it defaults to None, so that this method never raises a KeyError.
#       """)
# print("The employee id is " , d.get('employee_id'))
# print("The employee id1 is " , d.get('employee_id1'))
# print("The employee id1 is " ,d.get("employee_id1","Default_value"))

# ## Select/retrieve all items
# ## functions to get only keys , values , items
# print("""
#       The objects returned by dict.keys(), dict.values() and dict.items() are view objects.
#       They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes.
      
#       items()
#         Return a new view of the dictionary’s items ((key, value) pairs). See the documentation of view objects.

#       keys()
#         Return a new view of the dictionary’s keys. See the documentation of view objects.
      
#       values()
#         Return a new view of the dictionary’s values.
#       """)

# print(d.items())
# for key,value in d.items():
#     print(f'The {key} is {value}')    

# #Select/retrieve only values 
# print(d.values()) 
# for value in d.values():
#     print(f'value is {value}')    

# #Select/retrieve only keys  
# print(d.keys())
# for key in d.keys():
#     print(f'The key is {key}')    

# ADD
# single element  
# d['country']     = "India"
# print(d)

# # multiple elements ( merge operations though so just pass keys that are not in first dictionary)
# print(""" 
#       d |= other
#         Update the dictionary d with keys and values from other,
#         which may be either a mapping or an iterable of key/value pairs. 
#         The values of other take priority when d and other share keys.
#       """)

# print(d)
# d|= {"new_key":1,"new_key1":2}
# print(d)

# d.update( {"new_key":1,"new_key1":2})
# print(d)

# # UPDATE 
# # single element/ key 
# print("d[key] = value --Set d[key] to value.")

# d['employee_id']     = 99999999
# print(d)

# # if they key  is not present it adds so technically its a merge
# d['employee_id1']     = 888888888
# print(d)

# ##update single / multiple keys (merge) 
# print(""" 
#       update([other])
#         Update the dictionary with the key/value pairs from other, overwriting existing keys. Return None.
#       """)

# d.update({'employee_id': 77777777777})
# print(d)

# d.update({'employee_id': 6666666666666,'address': "new_address"})
# print(d)


# # multiple elements ( merge operations though so just pass keys that are there in first dictionary)
# print(""" 
#       d |= other
#         Update the dictionary d with keys and values from other,
#         which may be either a mapping or an iterable of key/value pairs. 
#         The values of other take priority when d and other share keys.
#       """)


# print(d)
# d|= {'employee_id': 6666666666666,'address': "new_address"}
# print(d)


# # delete 
# print("del d[key] -- Remove d[key] from d. Raises a KeyError if key is not in the map.")
# del d['employee_id']
# print(d)
# del d["name1"] # KeyError: 'name1'


# print("""
#       pop(key[, default])
#         If key is in the dictionary, remove it and return its value, else return default. 
#         If default is not given and key is not in the dictionary, a KeyError is raised.
#       """)

# my_dict = {"name": "gaurav", "rollno": 1 , "city": "Pune","Subjects" : ["DBDA","DIOT","DAC","HPCSA"]}
# print(my_dict)
# print("Popped value is " , my_dict.pop("name"))
# print("Popped value is ", my_dict.pop("name1")) # KeyError: 'name1'
# print("Popped value is ",my_dict.pop("name1","defaulted"))
# print(my_dict)

# print("""
#       popitem()
#         Remove and return a (key, value) pair from the dictionary. Pairs are returned in LIFO order.
#       """)
# print("before",my_dict)
# print("Popped last item: ",my_dict.popitem())
# print(my_dict)

# # ------------------
# # Other misc functions from the documentation
# # ------------------
# print("Changed in version 3.7: Dictionary order is guaranteed to be insertion order. ")
# print("""Please do not rely on the insertion order for dictionary since it is newly introduced
#       older implementation were not backported hence your same code may fail if you are on
#       running it on version <3.7 and rely on insertion order for any logic of any kind
#       """)

my_dict = {
           "name": "gaurav",
           "rollno": 1 ,
           "city": "Pune",
           "Subjects" : ["DBDA","DIOT","DAC","HPCSA"]
          }

# print(my_dict)
# print("list(d) -- Return a list of all the keys used in the dictionary d.")
# print(my_dict.keys()) # dict_keys(['name', 'rollno', 'city', 'Subjects'])
# print(list(my_dict))


# print("len(d) --Return the number of items in the dictionary d.")
# print(len(my_dict))

# print("key in d -- Return True if d has a key key, else False.")
# print("name" in my_dict)
# print("name1" in my_dict)

# print("key not in d -- Equivalent to not key in d.")
# print("name" not in my_dict)
# print("name1" not in my_dict)

# print("clear() -- Remove all items from the dictionary")
# print(my_dict)
# my_dict.clear()
# print(my_dict)

# print("copy() --Return a shallow copy of the dictionary.")
# my_copy_dict = my_dict.copy()
# print(my_dict)
# print(my_copy_dict)


# print("""
#       reversed(d)
#       Return a reverse iterator over the keys of the dictionary. This is a shortcut for reversed(d.keys()).
#       """)

# print(my_dict)
# print(list(my_dict.keys()))
# print(list(reversed(my_dict)))
# print(list(reversed(my_dict.keys())))
# print(list(reversed(my_dict.values())))
# print(dict(reversed(my_dict.items())))


# print("fromkeys(iterable[, value]) --Create a new dictionary with keys from iterable and values set to value.")
# population_density_statewise = dict.fromkeys(["MH","Punjab","Karnataka"],11)
# print(population_density_statewise)


# print("""
#       setdefault(key[, default])
#         If key is in the dictionary, return its value. 
#         If not, insert key with a value of default and return default. 
#         default defaults to None.
#       """) 
  
# print(my_dict)   
# print(my_dict.setdefault("name1","defaulted_value"))
# print(my_dict)   
# print(my_dict.setdefault("name1","new_defaulted_value")) # defaulted_value
# print(my_dict.setdefault("name2")) # None
# print(my_dict)   


# print("""
#       d | other
#         Create a new dictionary with the merged keys and values of d and other, 
#         which must both be dictionaries. 
#         The values of other take priority when d and other share keys.
#       """)
# my_dict = {"name":"gaurav" ,"address" : "Pune"}
# my_new_dict = {"name": "New name","rollno" : 1}
# print(my_dict)
# print(my_new_dict)
# print(my_dict|my_new_dict)
# print(my_dict)


# print("Dictionaries compare equal if and only if they have the same (key, value) pairs (regardless of ordering).")

my_dict = {"name" : "gaurav","rollno":1}
my_new_dict = {"rollno":1,"name" : "gaurav"}
my_newer_dict = {"rollno":1,"name" : "gaurav","state":"MH"}

print(my_dict == my_new_dict)
print(my_new_dict == my_newer_dict)



              
