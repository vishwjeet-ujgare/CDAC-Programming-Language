#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define N 100000
/*
                N  PRIME_NUMBER

                1           0
               10           4
              100          25
            1,000         168
           10,000       1,229
          100,000       9,592
        1,000,000      78,498
       10,000,000     664,579
      100,000,000   5,761,455
    1,000,000,000  50,847,534

*/
int main()
{
	int i, j;
	int count, flag;
	double exe_time;
	
	count = 1; // 2 is prime. Our loop starts from 3
		
	for(i=3;i<N;i++)
	{
	 	flag = 0;
		for(j=2;j<i;j++)	
	    	{
		    if((i%j) == 0)
		    {
			    flag = 1;
			    break;
		    }
	    	}
        	if(flag == 0)
        	{
            		count++;
        	}
	}
	
	
	printf("\n Number of prime numbers = %d \n", count);
	
}

