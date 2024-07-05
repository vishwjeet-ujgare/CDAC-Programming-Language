#include<stdio.h>
#include<stdlib.h>


int main()
{
	int size = 400 * sizeof(int);
	int a[400], aa[400];
	int i=0;
	

	//Initialize the vectors
	for(i=0; i<400; i++ )
	{
		a[i] = i;
	}

	// Add two vectors
	for(i=0; i<400; i++ )
	{
		aa[i] = (a[i]*a[i]);		
	}

	// print the output
	for(i=0; i<400; i++ )
	{
		printf("\t%d",aa[i]);
	}	
}




