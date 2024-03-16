#include <iostream>
#include <string.h>
using namespace std;

class Student
{
public:
    int id;
    char name[10];
    // string name;
    float per;
    char grade;
    int marks[5];
    int totalMarks;
    int totalSubject = 5;

    void diplayStudentDetails(Student &s)
    {
        cout<<"----------------------------"<<endl;
        cout << "ID : " << s.id << endl;
        cout << "Name :" << s.name << endl;
        cout << "percentage :" << s.per << endl;
        cout << "grade :" << s.grade << endl;
    }

    void userInput(Student &s)
    {

   
        s.totalSubject = totalSubject;

        cout << endl;
        cout << "Enter details for student id : " << s.id << endl;
        cout << "Enter Student Name : ";
        cin >> s.name;

        cout << "Enter Student Marks for " << s.totalSubject << " subjects" << endl;
        for (int i = 0; i < s.totalSubject; i++)
        {
            cout << i+1 << ". ";
            cin >> s.marks[i];
            cout << endl;
        }
    }
};
