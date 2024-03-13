#include <stdio.h>

void swapNumbers(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int num1, num2;

   
    printf("Enter first number: ");
    scanf("%d", &num1);
    printf("Enter second number: ");
    scanf("%d", &num2);

  
    printf("Original numbers: %d and %d\n", num1, num2);

  
    swapNumbers(&num1, &num2);

    
    printf("Swapped numbers: %d and %d\n", num1, num2);

    return 0;
}