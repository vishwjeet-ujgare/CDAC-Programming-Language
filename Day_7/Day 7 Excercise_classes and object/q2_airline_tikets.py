# -------------------------------------------
# Exercise 02 : Classes and objects -- try creating this in oops world
# -------------------------------------------
 
# Create a class that captures airline tickets. 
# Each ticket lists the departure and arrival cities, a flight number, and a seat assignment. 
# A seat assignment has both a row and a letter for the seat within the row (such as 12F). 

# main method:
# Make two examples of tickets being sold to passengers.
# display tickets booked details 


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

# main method
def main():
    seat1 = Seat(1214, "I")
    ticket1 = AirlineTicket("Mumbai", "Pune", "12F", seat1)
    ticket1.display_details()

    seat2 = Seat(1445, "I")
    ticket2 = AirlineTicket("Beed", "Pune", "15D", seat2)
    ticket2.display_details()
    
main()