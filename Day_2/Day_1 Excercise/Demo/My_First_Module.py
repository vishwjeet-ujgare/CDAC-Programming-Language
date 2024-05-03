""
''
""" """
''' '''

print("\n")
# This is a Single line comment 

print("Welcome to the world of Python Programming")

print("")

# variable/reference to the different datatypes objects creation 
my_name = "vishwjeet"
my_rollno  = 14
my_percentage  = 85.60
my_string = "This is string content"
my_char_string = "j"


# printing each of the variables/references 
print("my_name is " , my_name )
print("my_rollno is " , my_rollno )
print("my_percentage is " , my_percentage )
print("my_char_string is " , my_char_string )

print("")


# variable/reference to the different datatypes objects creation 
my_list = [1,2,3,3,3,"Hello","CDAC",3,3,3]
my_dict = {"name" : "Vishwjeet" , "rollno" : 14,'courseName':"HPCAP"}
my_tuple = (1,2,3,30,30,3,43,365,3)
my_set = {1,2,3,3,33,3,3,3,10,15,18,19,16,17,18,16}


#builtins.print("Datatype of my_name reference variable is " , type(my_name))
print("Datatype of my_name reference variable is " , type(my_name))
print("Datatype of my_percentage reference variable is " , type(my_dict))

print()

print("My all element in the list is :" ,my_list)
print("My first element in the list is " , my_list[5] )
print()


print("My all elements in the tuple is " , my_tuple )
print("My first element in the tuple is " , my_tuple[0] )
print()


print("My all element in the string is :" , my_string )
print("My first element in the string is :" , my_string[1] )
print()

print("My all element in the dictionary is :" , my_dict )
print("My my_name element in the dictionary is " , my_dict["courseName"] )
print()

print("My all element in the set is " , my_set )
print()


#
#
#
# taking my first input from the user
print("====================================\nTaking Input From the User\n====================================\n")

# my_first_input_var = input("Please provide some  input :")
# print("     > The value you inserted is " , my_first_input_var)
# print("     > The datatype of the value you inserted is " , type(my_first_input_var))

# print()

#
#
#
#
# defining constants in Python

print("=======================================\nDefining Constants in Python\n======================================")

MY_CONSTANT = 8
print(MY_CONSTANT)

MY_CONSTANT = 10 
print(MY_CONSTANT)
print()


# literals
print("=======================================\nliterals\n======================================")

a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

print(a)
print(b)
print(c)
print(d)


#Float Literal
print("\n=======================================\nFloat Literal\n======================================")

float_1 = 10.5 
float_2 = 1.5e2    # 1.5 * 10 raise to 2 / 1.5*(10**2 )


print(float_1, float_2)
print()

#Complex Literal 
print("\n=======================================\nComplex Literal  Literal\n======================================")

x = 3.14j
print(x)
print(x.imag, x.real)


print("\n=======================================\nStrings in Python\n======================================")

# Strings in Python
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string 
                  with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
unicodeA=u"\u2764"
unicodeB=u"\u2728"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(unicodeA)
print(unicodeB)
print(raw_str)


print("\n=======================================\nBoolean Operations\n======================================")
# Boolean Operations

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("""
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10
""")
print("OUTPUT :")
print("     > x is", x)
print("     > y is", y)
print("     > a:", a)
print("     > b:", b)


print("\n=======================================\n formatting in print Operations\n======================================")
# formatting in print

print("""\nprint(string1","string2","string3",sep = '*******' , end = '---------')""")
print("\nOUTPUT")

print("     > string1","string2","string3",sep = '*******' , end = '---------')

print("this is the next line.")

print("\n-----------------------------")

print("my name is " , my_name , "my_rollno is ",my_rollno)
print(f"my name is {my_name} my_rollno is     {my_rollno}" )



print("\n=======================================\n # is and is not operator \n======================================")
#
#
#
# is and is not operator 
print("""
      var1= [1,2,3]
      var2=var1
      var3=[1,2,3]
      


if var1==var3 :
    print("Same contents")
else:
    print("different contents")    

if var1  is var2 :
    print("Same object in memory")
else:
    print("different object in memory")   

if var1  is not var2:
    print("Same object in memory")
else:
    print("different object in memory")  
   
    
      """)

var1= [1,2,3]
var2=var1
var3=[1,2,3]

print("OUTPUT :")

if var1==var3 :
    print("Same contents")
else:
    print("different contents")    

if var1  is var2 :
    print("Same object in memory")
else:
    print("different object in memory")   

if var1  is not var2:
    print("Same object in memory")
else:
    print("different object in memory")  
