// reverse given number 

#include<stdio.h>

void main()
{
    int num;
    printf("-----reverse given number ---");
    printf("Enter a given number : ");
    scanf("%d",&num);

    // int tem=num;
    int rev=0;
     
    while(num>0)
    {
        int l=0;
        int ltempNum=num;
      //  calculating number of digits in number
        while(ltempNum>0)
        {
            ltempNum/=10;
            l++;
        }
        
        
        int j=1;
        int rem=num%10;

//multiplying according to length
        
        for(j;j<l;j++)
        {
          rem=rem*10;

        }

// adding remainder
        rev+=rem;

        num/=10;
        // printf("length of number is %d \n",l);
        printf("Reverse number is %d ",rev);
        

       
        
    }
}