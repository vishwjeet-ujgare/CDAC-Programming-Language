"""5) Take input of age of 3 people by user and determine oldest and youngest among them."""

from day2_exercise_functionality import takeIntValueFromUserPassMsg,printYoungAndOldAmongThem

p1_age=takeIntValueFromUserPassMsg("Please Enter Person's 1 age : ")
p2_age=takeIntValueFromUserPassMsg("Please Enter Person's 2 age : ")
p3_age=takeIntValueFromUserPassMsg("Please Enter Person's 3 age : ")


# get the oldest and youngest people
printYoungAndOldAmongThem(p1_age,p2_age,p3_age)