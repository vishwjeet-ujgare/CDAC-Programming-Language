#include<stdio.h>

void main()
{
    int tableTill,i=1;

    printf("Printing alll table till number\n");
    printf("Enter number : ");
    scanf("%d",&tableTill);

    for(i;i<=tableTill;i++){
    printf("starting table of %d \n",i);
        int j=1;
        for(j;j<=10;j++)
        {
            printf("%2d x %2d = %3d \n",i,j,i*j);
        }


    }

}