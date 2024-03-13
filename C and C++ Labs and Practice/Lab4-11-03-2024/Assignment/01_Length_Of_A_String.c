#include<stdio.h>

void main()
{
    char str[20]="Vishwjeet";
    int count=0;


    while(str[count]!='\0')
    {
        count++;
    }

    printf("\n\nLength of string : %d",count);
}