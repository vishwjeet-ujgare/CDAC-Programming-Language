#include <iostream>
#include <string.h>
using namespace  std;


class Student{
public:
    int id=1;
    char name[10];
    // string name;
    float per;
    char grade;
    int marks[5];
    int totalMarks;
    int totalSubject=5;

void diplayStudentDetails(Student &s)
{   
    cout<<"ID : "<<s.id<<endl;
    cout<<"Name :"<<s.name<<endl;
    cout<<"percentage :"<<s.per<<endl;
    cout<<"grade :"<<s.grade<<endl;
}


void userInput(Student &s)
{


   float userInput;
   cout<<"Enter Student Details"<<endl;;

   s.id=id;
   s.totalSubject=totalSubject;

  

    cout<<"Enter Student Name : ";
    cin>>s.name;

    cout<<"Enter Student Marks for "<<s.
    totalSubject<<" subjects"<<endl;
    for(int i=0;i<s.totalSubject;i++)
    {
        cout<<i<<". ";
        cin>>s.marks[i];
        cout<<endl;
    }
    
}

};


