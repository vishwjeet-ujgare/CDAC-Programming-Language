// Greatest of 3 nums Or which nums are same 

#include<stdio.h>

void main()
{
    int a ,b,c,d=0;
    // 12,45,12
    printf("Enter three Number separated by Comma : ");
    scanf("%d,%d,%d",&a,&b,&c);

    printf("===================================\n");
    printf("Greatest number beetween %d,%d,%d is ",a,b,c);

    if(a>b && a>c){
        d=a;
  
    }else if (b>a && b>c)
    {
      d=b;
    }else if (c>a && c>b)
    {
       d=c;
    }

    if(a==0 && b==0 && c==0)
    {
        printf(" None \n all values are 0 \n");
        return;
    }else{
        if(a==b && a==c)
        {
            printf("None \n All value are equal \n ");
            return;
        }
    }

 printf("%d \n",d);
 printf("===================================\n");



        if(a==b)
        {
            printf("a and b are have equal values \n");
        }else if (a==c)
        {
            printf("a and c are have equal values \n");
        }else if (b==c)
        {
             printf("b and c are have equal values \n");
        }
    

         
// printf("Enter value are %d,%d,%d \n",a,b,c);

}