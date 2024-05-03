"""
Create a game for FIZZ BUZ and keeping playing with the user untill the user chooses to skip the game

"""

# Define a function called fizz_buzz that takes a number as input
# and prints "Fizz" if it is divisible by 3, "Buzz" if it is divisible by 5,
# and "Fizz Buzz" if it is divisible by both 3 and 5
def fizz_buzz():
    num = int(input("Please Enter a Number :"))

    if num %5==0 and num % 3 ==0 :
        print("Fizz Buzz")
    elif num%3 == 0 :
        print("Fizz")
    elif num%5 == 0 :
        print("Buzz")
    else:
        print("Invalid Input")

# Define a function called play_game 
# that runs an infinite loop and keeps calling the fizz_buzz function 
# until the user decides to stop playing
def play_game():
    while(True):
        fizz_buzz()	
        if input("\n Do you want to continue (Y/N)").lower() == 'n':
            break

# Call the play_game function to start the game
play_game()
