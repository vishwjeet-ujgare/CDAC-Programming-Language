#include<stdio.h>
#include<omp.h>

int main()
{
	int a=10;

	#pragma omp parallel for lastprivate(a)
	for(int i=8;i<10;i++)
	{
		//printf("initial value for thread  %d is %d\n",omp_get_thread_num(),a);
		
		a++;
		printf("a value for thread %d is %d \n\n",omp_get_thread_num(),a);
	}
	printf("a (outisde paralle region) = %d \n",a);
	return 0;

}

