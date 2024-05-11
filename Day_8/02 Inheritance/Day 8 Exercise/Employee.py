# -------------------------
# Exercise on Inheritance:
# -------------------------
# Create a base class named Employee as follows:
# Employee (
# -- class variables and methods
# 	organisation_name, 
# 	get_organisation_name(),
# 	set_organisation_name(org_name)

# -- instance variables and methods()
# emp_id,
# name,
# base_location,
# deployed_location,
# designation,
# salary ,
# get_employee_details() 	


class Employee:
    organisation_name="C-DAC"
    
    
    def __init__(self,emp_id,emp_name,base_loacation,deployed_location,designation,salary):
        self.emp_id=emp_id
        self.name=emp_name
        self.base_location=base_loacation
        self.deployed_location=deployed_location
        self.designation=designation
        self.salary=salary
        
        def get_employee_details(emp):
            print(f"emp Id :{emp.emp_id}\nname : {emp.name}\nbase location :{emp.base_location}\ndeployed location :{emp.deployed_location}\ndesignation :{emp.designation}\nsalary :{emp.salary}",sep="\n")
        
        @classmethod
        def get_organisation_name():
            return self.organisation_name

        @classmethod
        def set_organisation_name(org_name):
            self.organisation_name=org_name