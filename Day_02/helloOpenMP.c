#include<omp.h>
#include<stdio.h>
void try();
int main()
{
         #pragma omp parallel  num_threads(10)
	{
		printf("1.Hello world \n");
	}
	
         //omp_set_num_threads(4);
         #pragma omp parallel  num_threads(10)
	{
		printf("2.Hello world \n");
	}

try();
	return 0;
}

void try(){
#pragma omp parallel 
{

   printf("3.Try Hello world \n");
		
	
}
}
