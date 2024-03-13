#include <stdio.h>

int i=10 , j=10;
void main()
{
    if(i++>10 & j++ >10)
    {
        printf("1). %d ,%d ",i,j);
    }else
    {
        printf("2). %d ,%d ",i,j);
    }
}