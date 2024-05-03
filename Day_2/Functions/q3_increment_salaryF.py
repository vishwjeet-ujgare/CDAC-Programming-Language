# 3) Define a variable named "raise_salary_percentage" and get the salary raise 
# percentage from the user, Now apply the raise to an employee
# with harcoded data Name= 'gaurav' existing_salary = 900 INR and 
# print the incremented salary to the console


def apply_salary_raise(raise_percentage,existing_salary=900):
    raise_amount = existing_salary * (raise_percentage / 100)
    new_salary = existing_salary + raise_amount
    return new_salary
    
    
def print_details(new_salary,name="Gaurav",existing_salary = 900,):
    print(f"{name}'s salary was {existing_salary} INR, with a {raise_percentage}% raise, the new salary is {new_salary} INR")
 

raise_percentage = int(input("Enter the salary raise percentage : "))
print_details(apply_salary_raise(raise_percentage))
