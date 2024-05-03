# 6) Take the source, destination, fare in INR, discount_rate percentage from the user and display the 
# string ex: "Fare from mumbai to pune is 400 INR after applied discount of 5% it is 380 INR"

def get_user_input():
    source = input("Enter Your Source : ")
    destination = input("Enter Your Destination : ")
    existingFare = float(input("Enter current Fare : "))
    discount_rate_percentage = float(input("Enter discount percentage : "))
    return source, destination, existingFare, discount_rate_percentage

def calculate_discount(existingFare, discount_rate_percentage):
    discount_of_rupees = existingFare * (discount_rate_percentage / 100)
    return existingFare - discount_of_rupees

def print_result(source, destination, existingFare, discount_rate_percentage, total_amount_after_discount):
    if total_amount_after_discount < 0:
        print("Enjoy Free ride from ", source, " To ", destination)
    else:
        print(f"Fare from {source} To {destination} is {existingFare} INR after applied discount of {discount_rate_percentage} % it is {total_amount_after_discount} INR")




source, destination, existingFare, discount_rate_percentage = get_user_input()

total_amount_after_discount = calculate_discount(existingFare, discount_rate_percentage)

print_result(source, destination, existingFare, discount_rate_percentage, total_amount_after_discount)
