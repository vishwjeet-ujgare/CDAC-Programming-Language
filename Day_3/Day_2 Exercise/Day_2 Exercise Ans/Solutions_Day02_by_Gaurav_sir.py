
# Take values of length and breadth of a rectangle from user 
# and check if it is square or not.

if int(input("length:")) == int(input("breath:")):
   print("Square")
else:
   print("Not Square")      

# 2) Take two int values from user and print greatest among them   

value1= int(input("value1:"))
value2 = int(input("value2:"))

if  value1>value2 :
   print("value1:",value1)
else:
   print("value2:",value2)

# 3) A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

total_cost = int(input("quantity")) *100
if total_cost >1000:
   print(round(total_cost - total_cost*.1))
else:
      print(total_cost)   

# 4) A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade

marks = int(input("marks"))
if marks < 25 :
   print("F")
elif  marks < 45 :  # marks >= 25 and marks < 45 :
   print("E")
elif marks < 50 :
   print("D")
elif marks <60 :
   print("C")
elif marks < 80 :
   print("B")
elif marks <=100 :
   print("A") 
else:
   print("Invalid number")   
   
# 5) Take input of age of 3 people by user and determine oldest and youngest among them.

person1= int(input("person1"))
person2= int(input("person2"))
person3= int(input("person3"))

# oldest
if (person1 > person2):
   if (person1 > person3):
      print("oldest:",person1)
   else:   
      print("oldest:",person3)
else:
   if (person2 > person3):
      print("oldest:",person2)
   else:   
      print("oldest:",person3)      

# youngest
if (person1 < person2):
   if (person1 < person3):
      print("youngest:",person1)
   else:   
      print("youngest:",person3)
else:
   if (person2 < person3):
      print("youngest:",person2)
   else:   
      print("youngest:",person3)            

# 6) A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

number_of_classes_held = int(input("Number of classes held"))

number_of_classes_attended= int(input("Number of classes attended."))

percentage = number_of_classes_attended / number_of_classes_held *100

if percentage >= 75 :
   print("student is allowed to sit in exam since percentage is ", round(percentage))
else:   
   print("student is NOT allowed to sit in exam since percentage is ",round(percentage))   