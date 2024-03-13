#include<iostream>

using namespace std;

class Emplyoee{
    
public:
int id;
char name[50];
float basic;
float hra;
float da;
float ta;
float salary;


void displayEmployee()
{
    cout<<"Id : "<<id <<endl;
    cout<<"Name : "<<name<<endl;
    cout<<"basic : "<<basic<<endl;
    cout<<"hra :"<<hra<<endl;
    cout<<"da :"<<da<<endl;
    cout<<"ta :"<<ta<<endl;
    cout<<"salary :"<<salary<<endl;
}


void calculateSalary()
{
    da =basic*0.18;
    hra=basic*0.15;
    ta=basic*0.1;

    salary=basic+da+hra+ta;
}

void appraiseEmployeeSalary()
{
    basic+=basic*0.05;
    calculateSalary();
    displayEmployee();
}


};

int main()
{
    Emplyoee e;
    
    cout<<"Enter id , name , basic : "<<endl;
    cin>>e.id>>e.name>>e.basic;
    

    e.calculateSalary();
    e.displayEmployee();
    e.appraiseEmployeeSalary();
    
}

