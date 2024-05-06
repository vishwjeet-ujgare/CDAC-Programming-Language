"""------------
File handling
-------------"""

# # Python program to demonstrate  opening a file
# file1 = open(r'C:\Users\HPCAP\Desktop\gaurav\test\my_first_file.txt','rt')
# print(file1.read())
# print("Before closing explicitly" , file1.closed)  
# file1.close()
# print("After closing explicitly" , file1.closed)  



# # no need to close if we use with context
# print("Read call below \n -----------------------")

# with( open('my_first_file.txt',"r") as file1):
#     print("Before coming out of with block " , file1.closed)   
#     print(file1.read())
# print("After coming out of with block " , file1.closed)   



# print("Readline call below \n -----------------------")
# with( open('my_first_file.txt',"r") as file1):
#     print(file1.readline(),end= "---\n")

# print("Readlines call below \n -----------------------")
# with( open('my_first_file.txt',"r") as file1):
#     print(file1.readlines(),end= "---\n")


# print(r" strip off those \n at the end of the list ")
# with ( open('my_first_file.txt',"r") )as file1:
#     lines = []
#     for line in file1:
#         lines.append(line.strip())
# print(lines)        

# print(" Write to a file in w mode ")
# with ( open('my_first_file.txt',"w") as file1):
#     file1.write("hi there \nhow are you doing ")

# print(" Write to a file in a mode ")
# with ( open('my_first_file.txt',"a") as file1):
#     file1.write("\nThis a new line ")

# # read is the primary functionality write is just added as secondary
# with( open('my_first_file.txt',"r+") as file1):
#     print(file1.read())
#     file1.write("\nI am writing")
  
# # write is primary read is secondary functionality
# with( open('my_first_file.txt',"w+") as file1):
#     print(file1.read())
#     file1.write("hello")

# # append is the primary objective , read functionality is added
# with( open('my_first_file.txt',"a+") as file1):
#     file1.write("I appended this line in append+ mode")
#     file1.seek(0)
#     print(file1.read())


# # Python program to demonstrate  opening a file in binary mode
# file1 = open('my_first_file.txt',"rb")
# print(file1.read())
# file1.close()

# # # # Python program to demonstrate  writing a file in binary mode
# file1 = open('my_first_file.txt',"w+b")
# file1.write(b'how are you doing')
# file1.close()

# """
# # Key takeaways
# 1) Open => ( read / write / append) => close 
# 2) open modes ( r,w,a,x,r+,w+,a+)
# 3) text / binary format
# """

# #lets you know if the file handle is closed or not 
# print(file1.closed)

# # Python program to demonstrate  opening a file with some exception handling
# try:
#     file1 = open('my_first_file.txt',"r")
#     print("I am reading the existing file -->\n", file1.read())
# except FileNotFoundError:
#     print("File Not present , I am goind ahead and creating a file for you with some default text !!! ")    
#     file1 = open('my_first_file.txt',"w+")
#     file1.write("AB")
#     # file1.writelines(['first_line\n','second_line\n','third_line'])
    
#     print("I am location ", file1.tell()) #2
#     print("I am resetting it at 0 " , file1.seek(0)) 
#     print("I am location after resetting ", file1.tell()) #0
#     print("I am reading just after writing-->", file1.read())
#     file1.close()



### Reading a File that has JSON 
import json

# The json.load() function reads a JSON file and parses it into a Python dictionary.
with open("person.json", "r") as fh:
    data = json.load(fh)
    
print(type(data)    )
print(data    )

data["name"] = "from_file"
data["address"] = "Pune"

print(data)    
# The json.dump() method directly writes a Python dictionary to a file in JSON format.
with open("person_modified.json", "w") as outfile:
    json.dump(data, outfile)
    
