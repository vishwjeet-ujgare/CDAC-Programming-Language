# 6) A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.


number_of_classes_held = int(input("Number of classes held : "))

number_of_classes_attended= int(input("Number of classes attended :"))

percentage = number_of_classes_attended / number_of_classes_held *100

if percentage >= 75 :
   print("student is allowed to sit in exam since percentage is ", round(percentage))
else:   
   print("student is NOT allowed to sit in exam since percentage is ",round(percentage))