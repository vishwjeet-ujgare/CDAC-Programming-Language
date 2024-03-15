#include <iostream>
#include <string>
using namespace std;

class Employee
{
public:
    int id;
    string name;
    float salary;

    Employee()
    {
        id=1;
        name="Jeet";
        salary=50000;

        cout<<"constructor called for id "<<id<<" : "<<endl;
    }

  
    Employee(int id, string name, float salary)
    {
        this->id = id;
        this->name = name;
        this->salary = salary;

    cout<<"Prameterise constructor called for id "<<id<<" : "<<name<<endl;
    }

        ~Employee()
    {
        
         cout<<"----XXXX Destructor called for id "<<id<< ":  ----XXXX "<<name<<endl<<endl;
    }


   
};

int main()
{

    

    Employee();

    Employee e2(2, "Jane Doe", 12346.7);
    // e2.print();

    Employee();

    return 0;
}