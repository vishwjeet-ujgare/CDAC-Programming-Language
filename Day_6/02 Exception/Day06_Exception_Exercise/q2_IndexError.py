
# 2) Write a program that creates a list of 5 elements of your choice 
# Now take the index that the user want the data of and print the value at that 
# location 
# Exception handle the code to  terminate gracefully by printing 
# Value not found if the index doesnot exists 



l=input("Enter 5 elements separated by space of your choice : ").strip()
l=(" ".join(l.split())).split()

print(l)

# # IndexError: list index out of range: if pass index that is not present
# i=int(input("Please enter index : "))
# print("Element at index ",i,"is : ",l[i])

#  ├── LookupError
#       │    ├── IndexError
#       │    └── KeyError
try:
    i=int(input("Please enter index : "))
    print("Element at index ",i,"is : ",l[i])
except IndexError:
    print("Please  enter valid index id , Index is not present")