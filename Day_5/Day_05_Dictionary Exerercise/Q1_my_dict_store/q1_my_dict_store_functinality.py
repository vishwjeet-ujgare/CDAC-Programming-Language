# Sample code template for my_dict_store
def startMenu():
    print("\n*************** Menu **********************")
    print("1.   Display number of elements in the capitals collection")
    print("2.   Add an element to the capitals collection like --> Afghanistan: Kabul")
    print("3.   Add multiple elements to the capitals collection like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella")
    print("4.   Remove an element from the collection") 	
    print("5.   Take a key from the user and show value if it is present in the dictionary")
    print("6.   Take a key from the user update it if it is present in the dictionary or add the key to the  dictionary")
    print("7.   EXIT")
    print("\n*******************************************")
    
def takeDecFromUser(capitals):
    if(input("Do you want to Create a dictionary OR want to use Default one : c/d : ").lower()== 'c'):
        createOwnDic(capitals)
    else:
        defaultDic(capitals)
        
def createOwnDic(capitals):
    try:
        dicLen=int(input("How many elements you want to add : "))
        for i in range(0,dicLen):
            keyName=input("Enter Key/state Name : ")
            value=input("Enter value/capital Name : ") 
            capitals[keyName]=value  
            print()   
    except ValueError:
        print("\nPlease Enter only integer number...")
        takeDecFromUser(capitals)
        
def defaultDic(capitals):
    capitals.update({
    "AN":"Andaman and Nicobar Islands",
    "AP":"Andhra Pradesh",
    "AR":"Arunachal Pradesh",
    "AS":"Assam",
    "BR":"Bihar",
    "CG":"Chandigarh",
    "CH":"Chhattisgarh",
    "DN":"Dadra and Nagar Haveli",
    "DD":"Daman and Diu",
    "DL":"Delhi",
    "GA":"Goa",
    "GJ":"Gujarat",
    "HR":"Haryana",
    "HP":"Himachal Pradesh",
    "JK":"Jammu and Kashmir",
    "JH":"Jharkhand",
    "KA":"Karnataka",
    "KL":"Kerala",
    "LA":"Ladakh",
    "LD":"Lakshadweep",
    "MP":"Madhya Pradesh",
    "MH":"Maharashtra",
    "MN":"Manipur",
    "ML":"Meghalaya",
    "MZ":"Mizoram",
    "NL":"Nagaland",
    "OR":"Odisha",
    "PY":"Puducherry",
    "PB":"Punjab",
    "RJ":"Rajasthan",
    "SK":"Sikkim",
    "TN":"Tamil Nadu",
    "TS":"Telangana",
    "TR":"Tripura",
    "UP":"Uttar Pradesh",
    "UK":"Uttarakhand",
    "WB":"West Bengal"
    })

def takeKeyValue():
    keyName=input("Enter Key/state Name : ")
    value=input("Enter value/capital Name : ")  
    return keyName, value
   
def dict_display_capitals(capitals): 
       for item in capitals.items():
           print(item)
     
def dict_add_element(capitals):
    keyName,value=takeKeyValue()
    capitals[keyName]=value
        
def dict_add_elements(capitals):
    dicLen=int(input("How many elements you want to add : "))
    for i in range(0,dicLen):
        dict_add_element(capitals)



def dict_remove_element(capitals):
    print("Enter Key Name that you want to Delete : ")
    del capitals[takeKeyName()]
    # capitals.pop(keyName)
    
def takeKeyName():
    return input("Enter Key Name : ")

def dict_show_value_for_a_key(capitals):
    print("Value for enter Key :",capitals[takeKeyName()])
     

def dict_update_or_add_a_key(capitals):
     keyName,value=takeKeyValue()
     capitals.update({keyName:value})
    #  capitals |={keyName:value}

def my_dict_store():
    print("\n Welcome to Our Dict Store !!! ")
	