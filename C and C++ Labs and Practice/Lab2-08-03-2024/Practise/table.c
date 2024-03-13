#include<stdio.h>

void main()
{
    int n;
    printf("Enter number to print table : ");
    scanf("%d",&n);

    int i=1;
    for(i;i<=10;i++)
    {
        printf("%d x %2d = %3d \n",n,i,n*i);
    }
}