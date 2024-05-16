#include<stdio.h>
#include<omp.h>


int main()
{
    omp_sched_t type =omp_sched_static;
    omp_set_schedule(type,2);

    #pragma omp parallel for schedule (runtime) num_threads(4)
    for (int i = 0; i < 20; i++)
    {
        printf("Thread %2d is running number %2d\n",omp_get_thread_num(),i);


    }
    
    return 0;
}