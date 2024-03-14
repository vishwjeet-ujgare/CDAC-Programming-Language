
#include <iostream>
#include "Student.h"
#include "Result.h"

using namespace  std;

int main()
{
    Student s1;
    Student s;
    Result r;

    s.userInput(s);
   
    // s.name="vishwjeet";
    r.calcMarks(s);
    r.calcPer(s);
    r.calculateGrade(s);
    s.diplayStudentDetails(s);



}