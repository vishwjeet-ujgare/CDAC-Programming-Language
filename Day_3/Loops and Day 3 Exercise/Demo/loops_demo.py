"""
initialisation
while (condition):
   body of while loop
   increment condition
   
range(start=0,stop,step=1)
   
"""

# # while 
# var = 1     # initialisation
# while(var < 5): # while (condition):
#    print(var) # body of while loop
#    var+=1 # increment condition
# print("Bye")   

# # do while construction
# var = 1     # initialisation
# while(True):
#    print(var) # body of while loop
#    var+=1 # increment condition\
   
#    if  var >= 5 :   # breaking condition
#       break
# print("Bye")  

# # range(start=0,stop,step=1)       

# print(list(range(0,4,1)))
# print(list(range(4)))
# print(list(range(0,4,2)))
# print(list(range(1,4,2)))
# print(range(1,4,2))
# print(list(range(5,2,-1)))

# for( int i = 0 , i< 4 ; i++ )
# {
#    printf("%d",i)
# }

# for i in range(0,4,1):
#    print(i)

# for i in "hello":
#    print(i)

# for i in [1,2,3,4]:
#    print(i)   
   

# for i in range(0,3,1):
#    temperature = 10
#    str2 = f"hello world temperature is  {str(temperature)} "
#    print(str2)

# # do while 
# while(True):
#    temperature = 10
#    str2 = f"hello world temperature is  {str(temperature)} "
#    print(str2)
   
   
#    if input("do you want to continue (y/n)").lower()  != 'y' :
#       break





# num=1 
# while(num<10):
#      print(num, end = " ")
#      num+=1
#      break

# num=1 
# while(num<10):
#      print(num, end = " ")
#      num= num + 1
#      continue
#      num= num + 1

# # if i want to print 1-5 but loop for 1-9
# num=1 
# while(num<10):
#      if num<6 : 
#         print(num, end = " ")
#      num+=1

# num=1 
# while(num<10):
#      if num<6 : 
#         print("running ", num)
#         break
#      num+=1
#      print(num, end = " ")


# num=1 
# while(num<10):
#      while(num<6 ): 
#         print("R", num , end = " " , sep = "")
#         break
#      num+=1
#      print(num, end = " ")

num=1 
while(num<10):
     while(num<6 ): 
        print("R", num , end = " " , sep = "")
        break
     num+=1
     if ( num < 6):
        continue
     print(num, end = " ")