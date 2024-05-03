# 3) A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

from day2_exercise_functionality import takeIntValueFromUserPassMsg,calculateTotalCostOfUnits

user_qnty=takeIntValueFromUserPassMsg("Enter many units you want to purchased : ")
print("Total cose for ",user_qnty," unit is ",calculateTotalCostOfUnits(user_qnty))
