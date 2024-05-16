#include<omp.h>
#include<stdio.h>

int main()
{
	int tid;
         omp_set_num_threads(5);

	#pragma omp parallel 
    	 {
		
		 
	                  tid=omp_get_thread_num();	 	
			 printf("Helllo World from %d of %d\n",tid,omp_get_num_threads());
		 

        }

              //	  printf( "Th.no : %3d inc x = %3d \n",omp_get_thread_num(),x);
return 0;
}

