# https://regexr.com/
import re

"""
[] . ^ $ * + ? {}
() \ |

#\w - Matches any alphanumeric character (digits and alphabets and underscore). 
    #\d - Matches any decimal digit. Equivalent to [0-9]
    #\s - Matches where a string contains any whitespace character.
    # Equivalent to [ \t\n\r\f\v].

"""
#------------------------------------
# DEMO 
#------------------------------------
# import re
# string0 = "abcdefghijklmnopqrstuvwxyz"
# string1 = "abcdefghijklmnopqrstuvwxyz1234567890"
# string2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# string3 = "0123456789"
# string4 = "HELLO HEL "
# string5 = "hello hel"
# string6 = "hello123"
# string14 = "hello123h"
# string7 = "123hello"
# string8 = "__"
# string9 = "......"
# string10 = "**************"
# string11 = "```````````````"
# string12 = "!!!!!!!!!!!"
# string13 = ""
# string15 = "abcdef highkl"
# string16 = "a430928409238409234"
# string17 = "a4"

# my_list = [string0,string1,string2,string3,string4,string5,string6,string14,string7,string8,string9,string10,string11,string12,string13,string15,string16,string17]
   
# for test_string in my_list:
#     result = re.findall(r"[a-z]+", test_string)  
#     search_obj = re.search(r"[a-z]+", test_string)  
#     if search_obj is not None :
#         print(f"{test_string} resulted into {result}")  
#         print(f"{test_string} resulted into {search_obj}")  



# Take the phone number and email of the user as input. 
# Users  having domain name @gmail.com 
# and number starting from +91 and followed by 10 digit (valid Indian number ) 
# should be accepted. 

# if inputs pass the validation then print "Welcome User" else print "Invalid credentials"        

import re
phone_number = "+91-9999999999"
email = "test@gmail.com"

if   re.search("@gmail.com$",email) and  re.search("^\+91-[0-9]{10}",phone_number) :
    print("Welcome User")
else:
    print("Invalid credentials!")      

   
"""
--------------------------------
Exercises -- Regular Expressions
-------------------------------
Given the list of strings as input :

gaurav1234@gmail.com
pratik190900234@gmail.com
2009_rocking_person@yahoo.com
GodFather2022@yahoo.com
Brocklesner_89_WWE@yahoo.com
TheRock_WWE@yahoo.com
JohnCena_WWE@yahoo.com
Undertaker_Roman_reigns@outlook.com
6789764666@rediffmail.com
Kane#6789@gmail.com


1) provide me the list of emails that do have special characters of #~`!
2) provide me the list of emails that start with numbers
3) provide me the list of emails that start with numbers followed by an underscore
4) provide me the list of emails that start with numbers followed by an underscore or small case characters
5) provide me the list of emails that start with numbers followed by an underscore or small case characters or large case characters
6) Provide me list of emails with only numbers before the @
7) Provide me list of emails with numbers anywhere before the @

"""

import re
string1 = 'gaurav1234@gmail.com'
string2 = 'pratik190900234@gmail.com'
string3 = '2009_rocking_person@yahoo.com'
string31 = '2009ROCKING_PERSON@yahoo.com'
string4 = 'GodFather2022@yahoo.com'
string5 = 'Brocklesner_89_WWE@yahoo.com'
string6 = 'TheRock_WWE@yahoo.com'
string7 = 'JohnCena_WWE@yahoo.com'
string8 = 'Undertaker_Roman_reigns@outlook.com'
string9 = '6789764666@rediffmail.com'
string10 = 'Kane#6789@gmail.com'

my_list = [string1,string2,string3,string4,string5,string6,string7,string8,string9,string10,string31]

# 1) provide me the list of emails that do have special characters of #~`!
pattern = "your_pattern_here"

for test_string in my_list:
    result = re.search(pattern, test_string)  
    if result :
        print(f"{test_string}")


    if result :
        print(f"{test_string}")

# #---------------------------------------------
# #*** Solutions to above Exercise ***
# #---------------------------------------------

# import re
# string1 = 'gaurav1234@gmail.com'
# string2 = 'pratik190900234@gmail.com'
# string3 = '2009_rocking_person@yahoo.com'
# string31 = '2009ROCKING_PERSON@yahoo.com'
# string4 = 'GodFather2022@yahoo.com'
# string5 = 'Brocklesner_89_WWE@yahoo.com'
# string6 = 'TheRock_WWE@yahoo.com'
# string7 = 'JohnCena_WWE@yahoo.com'
# string8 = 'Undertaker_Roman_reigns@outlook.com'
# string9 = '6789764666@rediffmail.com'
# string10 = 'Kane#6789@gmail.com'

# my_list = [string1,string2,string3,string4,string5,string6,string7,string8,string9,string10,string31]


# # 1) provide me the list of emails that do have special characters of #~`!
# # pattern = '[#~`!]'
# # 2) provide me the list of emails that start with numbers
# # pattern = '^\d'
# # 3) provide me the list of emails that start with numbers followed by an underscore
# # pattern = '^\d+_'
# # 4) provide me the list of emails that start with numbers followed by an underscore or small case characters
# # pattern = '^\d+[_a-z]'
# # 5) provide me the list of emails that start with numbers followed by an underscore or small case characters or large case characters
# # pattern = '^\d+[_a-zA-Z]'
# # 6) Provide me list of emails with only numbers before the @
# # pattern = '^\d+@'
# # 7) Provide me list of emails with numbers anywhere before the @
# pattern = '\d+@'

# for test_string in my_list:
#     result = re.search(pattern, test_string)  
#     if result :
#         print(f"{test_string}")