#include<omp.h>
#include<stdio.h>

int main()
{
	int x=0;
         omp_set_num_threads(200);
         #pragma omp parallel 
    	 {
		 x=x+1;
             //   printf( "Th.no : %3d inc x = %3d \n",omp_get_thread_num(),x);

        }

                printf( "Th.no : %3d inc x = %3d \n",omp_get_thread_num(),x);
return 0;
}

