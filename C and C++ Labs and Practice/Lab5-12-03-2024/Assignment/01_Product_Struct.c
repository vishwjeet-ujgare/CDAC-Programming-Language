#include<stdio.h>

struct product
{
    int pid;
    char name[20];
    float price;
    int isAvailable;
    int quntity; 

};

int main ()
{
   struct product p1;

printf("Enter product details. \n\tpid\n\tname \n\tprice\n\tisAvailable\n\tquntity");
printf("\nEnter : ");

scanf("%d %s %f %d %d",&p1.pid,&p1.name,&p1.price,&p1.isAvailable,&p1.quntity);

printf("Id =%d, Name =%s ,Price =%f, isAvailabe=%d ,qutity = %d",p1.pid,p1.name,p1.isAvailable,p1.quntity);
    
}