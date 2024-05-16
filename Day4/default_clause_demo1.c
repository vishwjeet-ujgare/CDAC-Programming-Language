#include<stdio.h>
#include<omp.h>


int main(){
	int x=10;
	int y=20;

	#pragma omp parallel num_threads(5) default(shared)  private(x)
	{
		printf("value of x =%d \n",x);
		x=omp_get_thread_num();
		printf("Thread %d : x = %d , y = %d \n",omp_get_thread_num(),x,y);

	}
	return 0;
}
