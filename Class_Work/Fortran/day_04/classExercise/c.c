#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define N 99999999

int main()
{
	int i, j;

	double area, pi;

	double dx, y, x;
	
	dx = 1.0/N;

	x = 0.0;

	area = 0.0;
	
	for(i=0;i<N;i++)
	{
		x = i*dx;
		y = sqrt(1-x*x);
		area += y*dx;
	}
	
	pi = 4.0*area;
	printf("\n Value of pi is = %.16lf\n ", pi);

    return 0;
}

// gcc c.c -lm