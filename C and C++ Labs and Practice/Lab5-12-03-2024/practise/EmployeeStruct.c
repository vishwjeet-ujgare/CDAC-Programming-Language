#include<stdio.h>

struct EmployeeStruct
{
    int id;
    char name[20];
    float salary;
};


int main()
{
    struct EmployeeStruct e;

    printf("Enter id , name , salary for the employee.\n");
    scanf("%d %s %f",&e.id,e.name,&e.salary);

    printf("Id=%d , Name=%s, Salary=%0.2f \n",e.id,e.name,e.salary);
    return 0;
}