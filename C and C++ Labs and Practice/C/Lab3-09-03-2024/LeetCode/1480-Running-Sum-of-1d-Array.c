/*
1480. Running Sum of 1d Array

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
*/

#include<stdio.h>

void main()
{
    int nums[4] = {1,2,3,4};
    int numssSize=4;

    int ans[numssSize];
  

    printf("array : ");
    int k=0; 
    for(k;k<numssSize;k++)
    {
        printf("%d ,",nums[k]);
    }

    printf("\n");

    
    ans[0]=nums[0];
    int sum=nums[0];

    int i =1;
    for(i;i<numssSize;i++)
    {
        sum+=nums[i];
        ans[i] =sum;

     }



    printf("Output ; ");
    k=0;
    for(k;k<numssSize;k++)
    {
        printf("%d ,",ans[k]);
    }
    printf("\n \n");
 

}