# Initial explaination for class and object creation

class Student:
    """ Student class stores name,rollno,pocketmoney and enrolled course"""
    # class variable
    school_name = "CDAC"    

    # initialiser
    def __init__(self,rcv_name,rcv_rollno,rcv_pocket_money,rcv_course):
        # instance variable
        self.student_name = rcv_name      # public instance variable 
        self.student_rollno = rcv_rollno   # public instance variable 
        self.student_pocket_money = rcv_pocket_money # public instance variable 
        self.student_enrolled_coursename = rcv_course # public instance variable 
        self.__student_bank_balance = set([298738,902803,72637,5625,565]).pop()
        print(f"{self} was created successfully with values {rcv_name},{rcv_rollno},{rcv_pocket_money},{rcv_course}")

    def __del__(self):
    # body of destructor   
        print("I am in destructor at address" , self )
        
    # instance method
    def get_enrolled_course(self):
        return self.student_enrolled_coursename

    # instance method
    def get_student_pocket_money(self):
        return self.student_pocket_money
    
    # instance method
    def enroll(self,rcv_course_name):
        self.student_enrolled_coursename = rcv_course_name

    # instance method
    def unenroll(self):
        self.student_enrolled_coursename = None
        
    # instance method
    def get_student_bank_balance(self):
        return self.__student_bank_balance

    # class method
    @classmethod
    def change_schoolname(cls,rcv_schoolname):
        cls.school_name = rcv_schoolname
    
    # static method
    @staticmethod
    def display_facilities_available():
        print("Facilities are 1) Gym ---- 2)Library ---- 3)TT\n")
    
# main method which is outside the class 
def main():
    print("I am in main and I am not part of the class ")

    # create a Student object referenced by gaurav
    gaurav= Student("Gaurav",1,100,'Python')
    duplicate_gaurav= Student("Gaurav",1,100,'Scala')
    
    # print(gaurav)
    # print(duplicate_gaurav)
    # # access the public instance variable for gaurav referenced object directly 
    # print("Before setting the public variable : ",gaurav.student_pocket_money) 
    # # set the public variable outside the class 
    # gaurav.student_pocket_money = 9999999
    # print("After setting the public variable : ", gaurav.student_pocket_money) 
    
    # # invoke a instance method(getter) for gaurav referenced object to access an attribute of the class 
    # print(gaurav.get_student_pocket_money())
    
    # print("Before Unenroll call ", gaurav.get_enrolled_course())
    # # invoke a instance method(setter) for gaurav referenced object to set an attribute of the class 
    # gaurav.unenroll()
    # print("After Unenroll call ", gaurav.get_enrolled_course())
    # # invoke a instance method for gaurav referenced object 
    # gaurav.enroll("Scala")
    # print("After Enroll call ", gaurav.get_enrolled_course())

    # create another Student object referenced by pratik
    pratik= Student("Pratik",2,200,'Java')
 
    # # trying to change the class variable using the Class reference 
    # # print the class variable using each of the available references 
    # print("School name at Class level was",Student.school_name)
    # print("Gaurav School name was",gaurav.school_name)
    # print("Pratik School name was",pratik.school_name)
    
    # # invoke class method(setter) using Student class reference
    # Student.change_schoolname("Sunbeam")

    # # print the class variable 
    # print("School name at Class level is",Student.school_name)
    # print("Gaurav School name is",gaurav.school_name)
    # print("Pratik School name is",pratik.school_name)

    
    # # invoke the static method 
    # Student.display_facilities_available()
    # gaurav.display_facilities_available()
    # pratik.display_facilities_available()
    # #display_facilities_available() # doesnot work 
    
    
    # try:
    #     print("gaurav bank balance is ", gaurav.__student_bank_balance)
    # except:
    #     print("Private variable accessed -- exception occured")
     
    # print("gaurav bank balance is ", gaurav.get_student_bank_balance())
    
    
    # Deleting Attributes student_pocket_money
    # print(gaurav.student_pocket_money)
    
    # AttributeError: 'Student' object has no attribute 'student_pocket_money'
    # del gaurav.student_pocket_money 
    # print(gaurav.student_pocket_money)
    # print(pratik.student_pocket_money)
    
    
    """  Deleting entire object gaurav
    The destructor was called after the program ended or when all the references to object are #deleted i.e when the reference count becomes zero, not when object went out of scope.
    """
    # # UnboundLocalError: local variable 'gaurav' referenced before assignment
    # del gaurav
    # print(gaurav.get_enrolled_course())
    
    # miscellnous functions for the class 
    # list all that the Student Class contains 
    print(dir(Student))
    print(Student.__doc__)
    
# invoke the main function 
main()


