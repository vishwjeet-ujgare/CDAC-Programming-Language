// Accept 5 marks as m1,m2,m3...m5 in int only
//   - Find percentage assume out of total =100;
//   - Find grade


#include <stdio.h>

void main()
{
    int c, java, python,AI,cloudComputing;
    float per;
  printf("Enter your 5 subject marks : \n")  ;

  printf("1. C :");
  scanf("%d",&c);

  printf("\n2. Java :");
  scanf("%d",&java);

  printf("\n3. Python :");
  scanf("%d",&python);

  printf("\n4. AI :");
  scanf("%d",&AI);

  printf("\n5. cloudComputing :");
  scanf("%d",&cloudComputing);

per=((c+java+python+AI+cloudComputing)/500.00)*100;

printf("==================================\n");
printf("Percentage of all five subject is : %f %%",per);
printf("\n==================================");

}