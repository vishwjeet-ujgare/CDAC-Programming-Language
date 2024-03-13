//WRT c programe that convert kilometer per hour to mile per hour
//  1 km/h = 0.62137 mph
#include<stdio.h>

void main()
{
    float km;
    float perKmH=0.62137f;
    float mile;

    printf("Enter number to convert KM to mile per hour : ");
    scanf("%f",&km);

    mile=km*perKmH;
    printf("%f km  per hour in mile is :%f \n",km,mile);



}