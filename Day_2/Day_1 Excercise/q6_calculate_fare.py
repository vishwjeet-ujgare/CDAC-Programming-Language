# 6) Take the source, destination, fare in INR, discount_rate percentage from the user and display the 
# string ex: "Fare from mumbai to pune is 400 INR after applied discount of 5% it is 380 INR"

source=input("Enter Yout Destination : ")
destination=input("Enter Yout Destination : ")
existingFare=float(input("Enter current Fare :"))

discount_rate_percentage=float(input("Enter discount percentage : "))
discount_of_ruppes=(existingFare*(discount_rate_percentage/100))

total_amount_after_discount=existingFare - discount_of_ruppes

print("")
if total_amount_after_discount <0:
    print("Enjoy Free ride from ",source," To ",destination) 
else:
    print(f"Fare from {source} To {destination} is {existingFare} INR after applied discount of {discount_rate_percentage} % it is {total_amount_after_discount} INR")
