#include<stdio.h>


int factorial(int num)
{
    if(num==1)
    {
        return 1;
    }
    else
    {
        return num*factorial(num-1);
    }
}

int main()
{
    int res=0;
    int userInput=5;
    res=factorial(userInput);
    printf("\nFactorial of number: %d = %d \n",userInput ,res);

    return 0;
}