def display_start_instructions():
    print("=============================================")
    print("-----!!! Welcome to Our List Store !!!------    ")
    print()
    
    print("Please enter a list with  seperated by Comma that you would want to perform Operation Upon")
    print()
    
    print("for ex: Pratiksha,Kevin,Sachin,Yuvraj,Sania")
    print("=============================================")
    
def display_menu():
    print("\n*************** Menu **********************")
    print("Operations supported by our program are :")
    print("  1:  Display all elements in the members list")
    print("  2:  Add an element to the members collection like 'Sehwag' ")
    print("  3:  Add elements to the members collection like ['David','Bret','Sanju']")
    print("  4:  Remove a member from the collection at a given subscript")
    print("  5:  Remove the last member from the collection ")
    print("  6:  Display third, fourth and fifth element from the collection ")
    print("  7: Exit the Program ")
    print("*******************************************")
    

def list_display_members(members,) :
    print("Your List : ",members)

def display_list_members_with_msg(members,msg) :
    print(f"{msg}",members)

def list_add_element(members) :
    new_element=input("Enter Element :")
    members.append(new_element)
    return members
	

def list_add_elements(members):
    print("Enter Elements Separated By Comma(,)")
    new_elements=input("Enter Elements Here : ").split(",")
    members.extend(new_elements)
    return members
	

def list_remove_element(members) :
    print("Enter Element index or Element that you want to delete")
    user_input=input("Enter Here : ")
    try:
        i = int(user_input)
        members.pop(i)
        print("After removing Elements at ",i,".")
        display_list_members_with_msg(members," New list :") 
        return members
    except ValueError:
        pass

    members.remove(user_input)
    print("After removing Elements ",user_input,".")
    display_list_members_with_msg(members,"New list :") 
    return members
    
	

def remove_last_element(members) :
    return members.pop()
	

def display_3_4_5_element(members):
    if(len(members)<5):
        print("Can't Delete: less than 5 members are in list.")
    else:
        print("Third, Fourth and Fifth elements : ",members[2:6])
	
