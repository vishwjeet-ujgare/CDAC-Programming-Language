#include <stdio.h>

struct Employee {
    char name[20];
    float salary;
    int age;
};

struct Employee* modify_struct(struct Employee *emp) {
    emp->salary += 100;
    emp->age += 1;
    return emp;
}

void printDetails(struct Employee empDetails) {
    printf("================\n");
    printf("Name is: %s\n", empDetails.name);
    printf("Salary is: %f\n", empDetails.salary);
    printf("Age is: %d\n", empDetails.age);
}

int main() {
    struct Employee empDetails;

    printf("=====Enter Employee Details====\n\n");

    printf("Enter Name: ");
    scanf("%s", empDetails.name);

    printf("Enter Salary: ");
    scanf("%f", &empDetails.salary);

    printf("Enter Age: ");
    scanf("%d", &empDetails.age);

    struct Employee *updateDetails = modify_struct(&empDetails);
    printDetails(*updateDetails);

    return 0;
}


