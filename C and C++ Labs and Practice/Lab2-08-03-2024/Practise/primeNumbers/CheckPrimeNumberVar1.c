#include<stdio.h>
// without using flag variable
void main()
{
    int n;
    printf("Enter number to chek whether number is prime or not : ");
    scanf("%d",&n);
    
    int i=2;
   while(i<n)
   {
        if(n%i==0)
        {
            break;
        }else{
            i++;
        }
   }

   if(i==n)
   {
    printf("%d is a prime number \n",n);
   }
   else{
    printf("%d is not a prime number \n",n);
   }
}