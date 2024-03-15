#include <stdio.h> 
  
 struct Employoee { 
    char  name[20]; 
    float salary ;
    int age ;

};



struct Employoee modify_struct(struct Employoee emp)
{
    emp.salary+=100;
    emp.age+=1;
    return emp;
};


void printDetails(struct Employoee  empDetails)
{
    printf("================\n");
  
    printf("Name is: %s\n",empDetails.name);
    printf("salary is: %f\n",empDetails.salary);
    printf("age is :%d\n",empDetails.age);

}

  
int main() 
{ 

struct Employoee  empDetails;

  printf("=====Enter Employee Details====\n\n");

    printf("Enter Name :");
    scanf("%s",&empDetails.name);

    printf("Enter Salary :");
    scanf("%f",&empDetails.salary);

    printf("Enter Age :");
    scanf("%d",&empDetails.age);

    // printDetails(empDetails);

   struct Employoee updateDetails=modify_struct(empDetails);
    printDetails(updateDetails);


    return 0; 
}
