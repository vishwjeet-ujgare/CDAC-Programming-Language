// print all prime numbers beetween given number
#include<stdio.h>

void main()
{
    int num;

    printf("----printing all prime number beetween given number------");
    printf("\nEnter a number :");
    
    scanf("%d",&num);

    int i=2;

    for(i;i<=num;i++)
    {
        int n=i;
        int j=2;

    
        while(j<n)
        {
            if(n%j==0)
                break;
            else    
                j++;
            
        }


        if(j==n)
             printf("%d,",n);
        
   }
         printf("\n");
    
}