#include<stdio.h>


int printTableRecursively(int count,int userInput)
{
    
    if(count<=10)
    {
         printf("\n%d x %2d = %2d",userInput,count,(userInput*count));
           return printTableRecursively(count+1,userInput);

    }
}

int main()
{
   int userInput=5,res;
  res= printTableRecursively(1,userInput);
 
    printf("\n\n output : %d",res);
 
    return 0;
}


// if(count==10)
    // {
    //     printf("\n%d x %2d = %2d",userInput,count,(userInput*count));
    //     return 10;
    // }
    // else
    // {
    //       printf("\n%d x %2d = %2d",userInput,count,(userInput*count));
    //       return printTableRecursively(count+1,userInput);
    // }