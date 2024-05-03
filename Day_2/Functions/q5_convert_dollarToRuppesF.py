# 5) Get the no of the dollars from the user apply the conversion of 
# 1 dollar = 82 rupees and print the amount to the console in rupees

def convert_dollars_to_rupees(dollars):
    rupees = dollars * 82
    print(f"{dollars} $ in rupees are {rupees}")

enteredDollar = int(input("Enter amount in Dollar : "))
convert_dollars_to_rupees(enteredDollar)