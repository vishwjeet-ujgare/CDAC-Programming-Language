#include<stdio.h>

void main()
{
    int n;
    printf("Enter number to print sum of all number until entered number : ");
    scanf("%d",&n);

    int i=1;
    int sum=0;
    for(i;i<=n;i++)
    {
        sum+=i;
    }
            printf("Sum of alll integer beetween 1 to %d = %d \n",n,sum);
}