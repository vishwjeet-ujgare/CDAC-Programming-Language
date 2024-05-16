#include<stdio.h>
#include<omp.h>


int main()
{

    #pragma omp parallel for schedule (static)
    for (int i = 0; i < 20; i++)
    {
        printf("Thread %2d is running number %2d\n",omp_get_thread_num(),i);


    }
    return 0;
}