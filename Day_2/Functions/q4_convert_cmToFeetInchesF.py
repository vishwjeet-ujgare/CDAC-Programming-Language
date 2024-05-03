# 4) Get the height from the user in cms and display the user height back to console
# in foot/feet and inches eg : 155 in cms displays 5.09 in feet and inches

def print_output(cm):
    print(f"{cm} cm in feet is {cmsToFeet(cm)} and In an Inches is {cmsToInches(cm)}")

def cmsToFeet(cm):
    return round((cm / 30.48), 2)

def cmsToInches(cm):
    return round((cm / 2.54), 2)
     
userHeight = float(input("Enter height in cms : "))
print_output(userHeight)