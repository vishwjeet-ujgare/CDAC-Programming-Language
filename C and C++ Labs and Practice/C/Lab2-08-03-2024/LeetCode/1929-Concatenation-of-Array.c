// 1929. Concatenation of Array
#include<stdio.h>

void  main() {
    
    //taking array form user 

    int nums[4]={2,3,4,5};
    int numsSize=4;

    int anssSize=numsSize*2;
    int ans[anssSize];
    
    int i,j;
    for(i=0,j=i+numsSize;i<numsSize;i++,j++)
    {

        ans[i]=nums[i]; 
        ans[j]=nums[i];
    }
 
 int k=0;
 for(k;k<anssSize;k++)
 {
    printf("%d ,",ans[k]);

 }
 printf("\n \n");
 
}