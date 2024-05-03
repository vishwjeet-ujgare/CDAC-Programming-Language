# 1) Accept two numbers from the user and print 
# a) addition 
# b) first number squared 2 
# c) first number raised to second number


a=int(input("Enter First Number : "))
b=int(input("Enter Second Number : "))

print("     1). You have entered a = ",a,", b = ",b)

sum=a+b
print("     2). Addition of ",a," and ",b , " is ",sum)

firstNumberSquare=a**2
print("     3). Square of ",a," is ",firstNumberSquare)

fNumRaisedToSecond=a**b
print("     4).",a," Raised to ",b," is ",a**b)