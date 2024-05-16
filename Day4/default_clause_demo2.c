#include<stdio.h>
#include<omp.h>


int main(){
	int x=10;
	int y=20;
	int z=5;
	#pragma omp parallel num_threads(5) default(shared) private(x,y)
	{
		printf("initial value of x = %d , y = %d \n", x,y);
		x=omp_get_thread_num(); // private copy of x for each thread
		y += x; //private coput of y each thread , each thread increments its private copy
		printf("Thread %d: x = %d , y = %d \n",omp_get_thread_num(),x,y);
		printf("value of z :%d ",z);
	}

	printf("outside parallel region : value of x = %d , y=%d \n",x,y);
	return 0;
}
