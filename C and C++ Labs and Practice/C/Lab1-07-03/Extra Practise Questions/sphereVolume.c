// 3. WRT C prg that calculate the Volume of a sphere   V = 4/3 π r³

#include <stdio.h>

void main()
{
    int r;
    float v;
    float py=3.14f;

    printf("Enter a radius of a sphere in number : ");
    scanf("%d",&r);
    
    v=(4.0/3.0)*py*(r*r*r);
    printf("Volume of given sphere is :%f \n",v);

}