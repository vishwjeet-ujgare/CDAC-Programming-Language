# Create a subclass of Employee named Manager as follows:
# Manager(
	
# 	-- instance variables and methods()
# 	
#   managed_employees[], # this is list of emp_references
# 	
#   perform_appraisal_for_an_employee(emp_reference,percent_raise),
# 	
#   get_manager_details()
# )





# Write a main method that does the following:
# create 3 objects of Employee 
# create an object of Manager_class and add the above 3 employee objects created as managed employees 
# display get_manager_details()
# for an employee do perform_appraisal_for_an_employee()

from Employee import Employee

class Manager(Employee):
    
    def __init__(self,emp_id,emp_name,base_loacation,deployed_location,designation,salary,managed_employee):
        self.managed_emp=managed_employee
        super().__init__(emp_id,emp_name,base_loacation,deployed_location,designation,salary)
        
        
    def get_manager_details(managerDetails):
        print(f"Manager Id :{managerDetails.emp_id}\nname : {managerDetails.name}\nbase location :{managerDetails.base_location}\ndeployed location :{managerDetails.deployed_location}\ndesignation :{managerDetails.designation}\nsalary :{managerDetails.salary}",sep="\n")


    def perform_appraisal_for_an_employee(managerObj1,incrementBy):
        for emp in managerObj1.managed_emp:
            print("Emp Id : ",emp.emp_id," , Emp Name : ",emp.name,"Salary : ",emp.salary)
        print("==============================")   
        
        empId=int(input("Enter Emp id for appraisal : "))  
        print("Enter employee id : ",empId)

        changeAppraisalForEmp=managerObj1.isEmpPresent(empId)
        # print("Before Appraisal : ",changeAppraisalForEmp.salary)
        if changeAppraisalForEmp==None:
            print("Given Employee id is not  present")
        else:
            empSalaryRaisedByRupess=(changeAppraisalForEmp.salary*(incrementBy/100))
            FinalSalary=changeAppraisalForEmp.salary+empSalaryRaisedByRupess
            changeAppraisalForEmp.salary=FinalSalary
            print("After Appraisal : ",changeAppraisalForEmp.salary)    

                    
    def isEmpPresent(managerObj1,empId):
        for e in managerObj1.managed_emp:
            if e.emp_id ==  empId:
                return e
            
        return None    

            
def main():
    print("Hello i am in main")
   
    # create 3 objects of Employee 
    e1=Employee(101,"Jeet","Beed","Pune","Team Lead",2000000)
    e2=Employee(102,"sonali","pune","Pune","senior developer",2200000)
    e3=Employee(103,"anmol","pimpari","Pune","software developer",2200000)
    

     # create an object of Manager_class and add the above 3 employee objects created as managed employees 
    managerObj1=Manager(1,"Deepshikha","Chhatisgad","Pune","Manager",3000000,[e1,e2,e3])

    print()
    managerObj1.get_manager_details()
    
    print("==============================")
    
    managerObj1.perform_appraisal_for_an_employee(10)
     
    print("==============================")
    
   
main()        