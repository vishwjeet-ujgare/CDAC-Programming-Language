# -------------------------------------------
# Exercise 02 : Classes and objects -- try creating this in oops world
# -------------------------------------------
 
# Create a class that captures airline tickets. 
# Each ticket lists the departure and arrival cities, a flight number, and a seat assignment. 
# A seat assignment has both a row and a letter for the seat within the row (such as 12F). 

# main method:
# Make two examples of tickets being sold to passengers.
# display tickets booked details 


# for generating random seat and flight purpose only
availableSeatsList={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
availableFlight={"A","B","C","D","E"}

class Seat:
    def __init__(self, row, letter):
        self.row = row
        self.letter = letter

class AirlineTicket:
    def __init__(self, departure_city, arrival_city, flight_number, seat):
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.flight_number = flight_number
        self.seat = seat

    def display_details(self):
        print()
        print(f"Departure City: {self.departure_city}")
        print(f"Arrival City: {self.arrival_city}")
        print(f"Flight Number: {self.flight_number}")
        print(f"Seat Assignment: {self.seat.row}{self.seat.letter}")

def getTravelDetails():
    startCity=input("Enter your city : ")
    destination=input("Enter your Destination city : ")
    
  
    return startCity,destination
# main method
def main():
    
    
    
    startCity,destination=getTravelDetails()
    ticket1 = AirlineTicket(startCity, destination, "12F", Seat(availableSeatsList.pop(),availableFlight.pop()))
    ticket1.display_details()


    print()
    startCity,destination=getTravelDetails()
    ticket2 = AirlineTicket(startCity, destination, "12F", Seat(availableSeatsList.pop(),availableFlight.pop()))
    ticket2.display_details()
    
main()