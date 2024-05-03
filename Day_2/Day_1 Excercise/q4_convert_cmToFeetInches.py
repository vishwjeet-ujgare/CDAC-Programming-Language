# 4) Get the height from the user in cms and display the user height back to console
# in foot/feet and inches eg : 155 in cms displays 5.09 in feet and inches

userHeight=float(input("Enter height in cms : "))

userHInfeet=round((userHeight/30.48),2)
userHInInches=round((userHeight/2.54),2)

print(userHeight," cmc in feet is ",userHInfeet," and In an Inches is ", userHInInches)
10
