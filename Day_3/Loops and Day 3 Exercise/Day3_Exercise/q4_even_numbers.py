# 4) Take a number from the user and print all Even numbers from 1 to that number 


# Get the number from the user
number_from_user = int(input("Please enter a number: "))

# Loop through all odd numbers from 1 to the number entered by the user (inclusive)
for i in range(1, number_from_user + 1, 2):
    # Print the current number
    print(i, end=" ")