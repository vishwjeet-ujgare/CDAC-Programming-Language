//check whether number is prime number or not using flag

#include<stdio.h>
#include<stdbool.h>

void main(){
    int num;
    bool isPrime = true;

    printf("\n----check whether number is prime number or not using flag---\n\n");
    printf("Please enter number: ");

    scanf("%d",&num);

   int i=2;

   for(i;i<=(num/2);i++)
   {
        if(num%2==0)
             isPrime=false;
             break;
      
   }

   if(isPrime)
        printf("%d is Prime \n",num);
    else
        printf("%d is Not a Prime \n",num);
   


}