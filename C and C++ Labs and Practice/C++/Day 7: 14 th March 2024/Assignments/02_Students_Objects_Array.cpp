// 2. Create an array of student class objects, accept data from user and
// display the data.

#include <iostream>
#include <string.h>
using namespace std;

class Student
{
private:
    int id;
    string name;

public:
    int GetId() const
    {
        return id;
    }

    void SetId(int id)
    {
        this->id = id;
    }

    string GetName() const
    {
        return name;
    }

    void SetName(string name)
    {
        this->name = name;
    }

    void displayDetails()
    {
        cout << "Id : " << id << endl;
        cout << "Name : " << name << endl;
    }
};

int main()
{

    int studentCount;

    cout << "-----Enter student details------" << endl;

    cout << "Enter student count : ";
    cin >> studentCount;

    cout << endl;

    Student students[studentCount];

    for (int i = 0; i < studentCount; i++)
    {
        Student s;

        int id;
        string name;

        cout << "Enter student Id : ";
        cin >> id;

        cout << "Enter student Name : ";
        cin >> name;

        s.SetId(id);
        s.SetName(name);

        students[i] = s;

        cout << "---------------------------" << endl;
    }

    cout << "-----Display student details------" << endl;
    for (int i = 0; i < studentCount; i++)
    {

        cout << "---------------------------" << endl;
        students[i].displayDetails();
    }
}