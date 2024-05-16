#include <stdio.h>
#include <omp.h>

int main(){
    int sum0 = 0, sum1 = 0, sum2 = 0, sum3 = 0;

    #pragma omp parallel num_threads(4)
    {
        #pragma omp for
        for (int i = 0; i <= 100; i++) {
            int tid = omp_get_thread_num();
            if (tid == 0) {
                sum0 += i;
            } else if (tid == 1) {
                sum1 += i;
            } else if (tid == 2) {
                sum2 += i;
            } else if (tid == 3) {
                sum3 += i;
            }
        }
        
        #pragma omp barrier
	#pragma omp single
    	{
          printf("Sum is : %d\n", sum0 + sum1 + sum2 + sum3);
        }

    }

    
    return 0;
}
