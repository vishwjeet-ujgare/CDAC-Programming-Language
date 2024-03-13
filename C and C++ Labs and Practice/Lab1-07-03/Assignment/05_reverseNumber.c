// Assume n =3 i.e three digit number  and reverse it 

#include <stdio.h>

void main()
{
    int num,rev=0;
    printf("Enter only any three digit integer number to reverse it : ");
    scanf("%d",&num);

    rev+=(num%10)*100;
        num/=10;

    rev+=(num%10)*10;
    num/=10;

    rev+=num;
    printf("%d",num%1);
   
    printf("Reverse of %d is %d",num,rev);

}