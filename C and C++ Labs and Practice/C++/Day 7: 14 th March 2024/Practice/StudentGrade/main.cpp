
#include <iostream>
#include "Student.h"
#include "Result.h"

using namespace  std;

int main()
{
    
 
       int totalStudents;

        cout << "Enter Student number : ";
        cin >> totalStudents;

        Student students[totalStudents];

        cout << endl;
        cout << "======Enter Student Details for" << totalStudents<<"====="<< endl;
        ;

    for(int i=0;i<totalStudents;i++)
    {
        Student s;
        s.id=i+1;
        s.userInput(s);
        students[i]=s;

    }



cout<<"==============Displaying students Details========================"<<endl;
   
   
    for(int i=0;i<totalStudents;i++)
    {

        Result r;
       Student s1= students[i];

    r.calcMarks(s1);
    r.calcPer(s1);
    r.calculateGrade(s1);
    s1.diplayStudentDetails(s1);
    }

    
   


}