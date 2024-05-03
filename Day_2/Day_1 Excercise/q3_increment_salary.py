# 3) Define a variable named "raise_salary_percentage" and get the salary raise 
# percentage from the user, Now apply the raise to an employee
# with harcoded data Name= 'gaurav' existing_salary = 900 INR and 
# print the incremented salary to the console


Name= 'Vishwjeet'
existing_salary = 900 
raise_salary_percentage=float(input("Enter raise salary percentage % : "))

raise_salary=(existing_salary *(raise_salary_percentage / 100))
total_increment_salary=existing_salary+raise_salary

print("Increment of ruppes ",raise_salary)
print("Total Incremented salary is ",total_increment_salary)