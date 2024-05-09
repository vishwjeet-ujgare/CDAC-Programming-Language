from  classes_objects_demo import Student
# """ Single Inheritance with nothing in the new child class """
# class Hpcap_student(Student):
#     pass

# Hrithik = Hpcap_student("Hrithik",3,300,"HPCAP")
# print(Hrithik.get_student_pocket_money())

""" Single Inheritance with functionality added/modified in the new child class """
class Hpcap_student(Student):

    # initialiser
    def __init__(self,rcv_name,rcv_rollno,rcv_pocket_money,rcv_course,rcv_alternate_skill_set = []):
        # call to # initialiser of the parent class Student
        super().__init__(rcv_name,rcv_rollno,rcv_pocket_money,rcv_course)
        
        # instance variable
        self.alternate_skill_set = rcv_alternate_skill_set
        print(f"{self} was created successfully with values {rcv_name},{rcv_rollno},{rcv_pocket_money},{rcv_course},{rcv_alternate_skill_set}")

    # instance method (getter)
    def get_alternate_skill_set(self):
         return self.alternate_skill_set

    # instance method (setter)
    def set_a_alternate_skill_set(self,rcv_new_skill):
         self.alternate_skill_set.append(rcv_new_skill)

    # instance method (setter)
    def set_many_alternate_skill_set(self,rcv_new_skills):
         self.alternate_skill_set.extend(rcv_new_skills)

    # overrided instance method 
    def unenroll(self):
        print("I have overrided this method from the parent class ")
        self.student_enrolled_coursename = "HPCAP"    

    # overloaded the overrided method unenroll instance method , it has shadowed the overrided method 
    def unenroll(self,bank_balance=100):
        print("I have new version of the over-rided  method from the parent class ")
        if bank_balance > 50000: 
            print("You cannot un-enroll finish your course !!")
        else:    
            self.student_enrolled_coursename = "HPCAP"    
            
    # overloading is not supported in python
    def display_string(self,str):
        print("display string version 1 : " , str)    

    def display_string(self,str,num):
        print("display string version 2 : " , str , num)    

# main method 
# create a Student object referenced by Hrithik
Hrithik = Hpcap_student("Hrithik",1,100,'Python',["C","C++","Python"])

# accessing things that the parent class provides and also defined in Hpcap_student class
print(Hrithik.student_enrolled_coursename)
Hrithik.unenroll()
print(Hrithik.student_enrolled_coursename)

# # add a skill to the object referenced by Hrithik
print(Hrithik.get_alternate_skill_set())
Hrithik.set_a_alternate_skill_set("Perl")
print(Hrithik.get_alternate_skill_set())

# add many skills to the object referenced by Hrithik
print(Hrithik.get_alternate_skill_set())
Hrithik.set_many_alternate_skill_set(["Docker","Git"])
print(Hrithik.get_alternate_skill_set())

Hrithik.display_string('test') # no overloading support
Hrithik.display_string('test',2)


