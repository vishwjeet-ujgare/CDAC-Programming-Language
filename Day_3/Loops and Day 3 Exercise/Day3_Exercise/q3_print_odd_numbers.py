#
# 3) Take a number from the user and print all Odd numbers from 1 to that number.
# Get the number from the user



number_from_user = int(input("Please enter a number: "))

# Initialize the current number being checked to 1
current_number = 1

# Loop through all numbers up to and including the number entered by the user

print("Odd Numbers till",number_from_user,": ",sep=" ",end=" ")
while(current_number <= number_from_user):
    # Check if the current number is odd
    if current_number % 2 != 0:
        # Print the current number if it is odd
        print(current_number, end=" ")
    current_number += 1