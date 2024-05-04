# 1) Write a program that creates a dictionary like this 
# {
#     1: "red" , 2: "Blue" , 3: "Orange"
# }

# Now take the key as input from the user and print its corresponding colour 
# (Exception handle the code to terminate gracefully by printing 
# Colour not found if the key doesnot exists )

colorDic={
    "1":"Red",
    "2":"Blue",
    "3":"Orange"
}

colorKey=input("Enter your color number :  ")

# #key error: if we pass key that is not present 
# print("Corresponding colour for your id :",colorKey,"is",colorDic[colorKey])

#  ├── LookupError
#       │    ├── IndexError
#       │    └── KeyError

try:
    print("Corresponding colour for your id :",colorKey,"is",colorDic[colorKey])
except KeyError:
    print("key is not present please try again ....")
