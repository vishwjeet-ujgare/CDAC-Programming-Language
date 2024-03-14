#include <iostream>
using namespace  std;


class Result{
public:

void calcMarks(Student &s)
{
    
    
    for(int i=0;i<s.totalSubject;i++)
    {
        s.totalMarks+=s.marks[i];
     
        
    }
   
}

void calcPer(Student &s)
{
    float outOf=s.totalSubject*100;
     s.per=(s.totalMarks/outOf)*100;
  }


void calculateGrade(Student &s)
{  
    float percentage=s.per;

    if(percentage>=0 && percentage<40)
    {
        s.grade='F';
    }
    else if(percentage>=40 && percentage<60)
    {
        s.grade='B';
    }
     else if(percentage>=60 && percentage<75)
    {
        s.grade='A';
    }
     else if(percentage>=75 && percentage<=100)
    {
        s.grade='O';
    }
}







};
