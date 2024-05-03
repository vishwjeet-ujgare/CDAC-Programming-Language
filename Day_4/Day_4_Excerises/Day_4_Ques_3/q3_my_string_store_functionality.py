
def display_menu():
    print("\n*************** Menu **********************")
    print("Operations supported by our program are :")
    print("  1:  Display the string")
    print("  2:  Display third, fourth and fifth element from the string ")
    print("  3:  Retrieve element at a given subscript")
    print("  4:  Retrieve elements from a given subscript and to a given subscript")
    print( " 5:	 Find minimum character in the string " )
    print( " 6:	 Reverse the string " )
    print( " 7:	 Output list of tuple( character,count) for each characters of the string  " )
    print( " 8:	 Output list of characters of the string that appear more than once " )
    print( " 9:  Check if the string is a palindrome and return output message accordingly")
    print("  10: Exit the Program ")
    print("\n*************************************")


def string_display(string_input) :
    print("Your String is : ",string_input) 

def display_3_4_5_element(string_input) :
    print("3 to 5 element of ",string_input,":",string_input[2:5]) 

def string_retrieve_element(string_input):
    try:
        i=int(input("Enter index of element that you want to retrive : "))
        print("Charcter at index ",i,":",string_input[i])
    except ValueError:
        print("Enter only int value..")
        pass

def string_retrieve_elements(string_input) :
    try:
        start=int(input("Enter Starting index : "))
        end=int(input("Enter Ending  index : "))
        
        if(len(string_input)<end):
            print("String has only ",end," elements.")
            return
        else:
            if(start==0):
                if input("Do you want to print from 1 element  y/n :").lower()=='y':
                    print(f"Elements from {start+1} to {end} : ",string_input[start:end])
                    return
               
        print(f"Elements from {start} to {end} : ",string_input[start:end]) 
    except ValueError:
        print("Please enter only integer values ...")
        pass

def find_min_element(string_input) :
    print("Minimum character in String is : ",min(string_input)) 

def reverse_string(string_input) :
    print("Reversed String : ",string_input[::-1] )
    

def  find_each_character_count(string_input):
     string_l=list(set(string_input))
     string_final_list=[]
     for i in string_l:
         c=string_input.count(i)
         string_final_list.append((i,c))
         
     print(string_final_list)
    

def  find_character_count_greater_than_1(string_input):
     string_l=list(set(string_input))
     string_final_list=[]
     for i in string_l:
         c=string_input.count(i)
         if(c>2):
            string_final_list.append(i)
         
     print(string_final_list)
    
        
     

def  check_palindrome(string_input):
   print(string_input,"palinfrome = >", string_input == string_input[::-1] )
             