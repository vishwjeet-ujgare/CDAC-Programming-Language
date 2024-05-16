#include<stdio.h>
#include<omp.h>

int main(){
	int array[]={1,2,3,4,5,6,15,20,7,8,9,10};
	int maxNum=0;

	#pragma omp parallel for reduction(max:maxNum)
	for (int i=0;i<array.length();++i){
		if(array[i]>maxNum){
			maxNum=array[i];
		}
		printf("Thread %d : Iteration %d ,m,max = %d \n",omp_get_thread_num(),i,maxNum);
	}

	printf("max : %d \n",maxNum);
	return 0;
}
