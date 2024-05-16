#include <stdio.h>      
#include <omp.h>
#include <stdlib.h>
#define N 1000

int getRandomNumber(int);
int arr[N];  
    
int  main()  
{     
           
   #pragma omp parallel num_threads(N) 
	for (int i = 0; i<1000; i++)
     	{
        	getRandomNumber(i);
        
     	}
     
     #pragma omp barrier
     int maxNum = arr[0]; 	
     #pragma omp single
     { 
     	
  
    	for (int i = 0; i < 1000; i++) { 
        	if (maxNum < arr[i]) 
           		maxNum = arr[i]; 
    		} 
      
      	}
      	
      	printf("Maximum Nuber is : %d",maxNum ); 
return 0;
  }
    


int getRandomNumber(int i)

{  
     int randomNum=rand()%1000;
     arr[i]=randomNum;
     //printf("The thread %d = %d \n",omp_get_thread_num(),randomNum); 
     return randomNum;
}  
