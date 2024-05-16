#include<stdio.h>
#include<omp.h>

int main()
{
	int x=2;

	omp_set_num_threads(5);
		printf("Before paraller  region x : %d,address =%p  \n",x,&x);
	#pragma omp parallel private(x)
	{
		printf("Initial value of in parrallel region x : %d,address =%p  \n",x,&x);
		//x=omp_get_thread_num();
		printf("Thread %d has private x=%d,address =%p \n",omp_get_thread_num(),x,&x);
		printf("---------------\n");
	}

	printf("after parallel region x : %d,address =%p \n",x,&x);
	return 0;
}

