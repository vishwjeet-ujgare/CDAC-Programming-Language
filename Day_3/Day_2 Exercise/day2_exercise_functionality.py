def isSquare(l,b):
    if l==b:
        return True
    else:
        return False

def takeFloatValueFromUser(howMuch):
    if(howMuch==1):
        first_value=float(input("Enter first flaot value  : "))
        return first_value
    elif (howMuch==2):
        first_value=float(input("Enter first flaot value : "))
        second_value=float(input("Enter  second flaot value : "))
        return first_value,second_value
    elif (howMuch==3):
        first_value=float(input("Enter first float value : "))
        second_value=float(input("Enter second flaot value : "))
        third_value=float(input("Enter third flaot value : "))
        return first_value,second_value,third_value
    

def takeFloatValueFromUserPassMsg(str):
    first_value=float(input(f"{str}"))
    return first_value
    
def takeIntValueFromUser(howMuch):
    if(howMuch==1):
        first_value=int(input("Enter first int value  : "))
        return first_value
    elif (howMuch==2):
        first_value=int(input("Enter first int value  : "))
        second_value=int(input("Enter second second value : "))
        return first_value,second_value
    elif (howMuch==3):
        first_value=int(input("Enter first int value : "))
        second_value=int(input("Enter second int value : "))
        third_value=int(input("Enter third int value : "))
        return first_value,second_value,third_value

def takeIntValueFromUserPassMsg(str):
    first_value=int(input(f"{str}"))
    return first_value

def takeAThreeStr(str):
    first_str=input(f"{str}")
    return first_str
    

def takeTwoStr(str1,str2):
    first_str=input(f"{str1}")
    second_str=input((f"{str2}"))
    return first_str,second_str

def greatestAmongTwo(num1,num2):
    if(num1>num2):
        return num1
    else:
        return num2

def calculateTotalCostOfUnits(qnty):
    if(qnty>10):
        actual_cost=(100 * qnty)
        discount_cost=actual_cost*(10/100)
        return (actual_cost-discount_cost)
    else:
        return (100*qnty)

def printCorrespondingGrade(m):
    if(m<25):
        return "F"
    elif m>=25 and m<45:
        return "E"
    elif m>=45 and m<50:
        return "D"
    elif m >=50 and m<60:
        return "C"
    elif m>=60 and m<80:
        return  "B"
    elif m>=80:
        return "A"


def printYoungAndOldAmongThem(person1,person2,person3):
     # oldest
    if (person1 > person2):
        if (person1 > person3):
            print("oldest:",person1)
        else:   
            print("oldest:",person3)
    else:
        if (person2 > person3):
            print("oldest:",person2)
        else:   
            print("oldest:",person3)      

    # youngest
    if (person1 < person2):
        if (person1 < person3):
            print("youngest:",person1)
        else:   
            print("youngest:",person3)
    else:
        if (person2 < person3):
            print("youngest:",person2)
        else:   
            print("youngest:",person3) 