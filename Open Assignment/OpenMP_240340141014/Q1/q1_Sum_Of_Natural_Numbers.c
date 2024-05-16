#include <stdio.h>
#include <omp.h>
#define N 4
int main(){
    int sum[N]={0};
    int total_sum=0;

    #pragma omp parallel num_threads(N)
    {
        #pragma omp for
        for (int i = 0; i <= 100; i++) {
            sum[omp_get_thread_num()] += i;
        }
        
        
    	
    }
    
    
    #pragma omp barrier
    total_sum = 0;
    #pragma omp for
    for (int i = 0; i < N; i++) {
       	total_sum += sum[i];
    	}
    printf("Sum is : %d\n", total_sum);

    

    return 0;
}
