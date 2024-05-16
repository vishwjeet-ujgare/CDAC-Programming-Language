#include <omp.h>
#include <stdio.h>

int main()
{

    omp_set_num_threads(3);
#pragma omp parallel sections
    {
        #pragma omp section
        {
            printf("This is section 1, executed by thread %d \n", omp_get_thread_num());
        }
        
        #pragma omp section
        {
            printf("This is section 2, executed by thread %d\n", omp_get_thread_num());
        }

        #pragma omp section
        {
            printf("This is section 3, executed by thread %d\n", omp_get_thread_num());
        }
        
        #pragma omp section
        {
            printf("This is section 4, executed by thread %d\n", omp_get_thread_num());
        }
}
    return 0;
}