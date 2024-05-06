# -------------------------------------------
# Exercise 01 : Classes and objects -- try creating this in oops world
# -------------------------------------------
# Employee
#   # instance variables 
#    emp_id
#    emp_salary
#    mgr_id


#   # class variable 
#   department_name
  
#   # instance methods
#   get_emp_salary()-> emp_salary
#   set_emp_salary(rcv_salary)-> emp_salary

#   # class method 
#   get_department_name() --> department_name
  
#   # static method
#   field_expertise() --> just displays some expertise for all my employees
  
# main:

# 1) create an object employee(100,1000,1)  
# 2) do the following for the created object
# // direct access using .notation
# empid
# emp_salary
# mgr_id
# 3) print the department name 
# 4) display the expertise for the employees 
# 5) Deleting Attributes and Objects


class Employee:
    # class variable
    department_name = "Engineering"

    def __init__(self, emp_id, emp_salary, mgr_id):
        # instance variables
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.mgr_id = mgr_id

    # instance method
    def get_emp_salary(self):
        return self.emp_salary

    # instance method
    def set_emp_salary(self, rcv_salary):
        self.emp_salary = rcv_salary

    # class method
    @classmethod
    def get_department_name(cls):
        return cls.department_name

    # static method
    @staticmethod
    def field_expertise():
        return "Expertise: Software Development"

# object employee
e = Employee(100, 1000, 1)

# accessing instance variables using dot(.) notation
print("\nEmployee ID:", e.emp_id)
print("Employee Salary:", e.emp_salary)
print("Manager ID:", e.mgr_id)

# printing  department name
print("\nDepartment Name:", Employee.department_name)

# display the static method
print("Static Method : ",Employee.field_expertise())

# deleting attributes and objects in Python is not necessary not neccessar python will delete it automatically
del e