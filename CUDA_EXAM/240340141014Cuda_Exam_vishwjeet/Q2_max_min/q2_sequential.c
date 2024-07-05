
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// #define SIZE 10000000
#define SIZE 10

int main() {
    int *arr = (int *)malloc(SIZE * sizeof(int));
    int max, min;

    // Initialize array with random values
    for (int i = 0; i < SIZE; i++) {
        arr[i] = rand() % 100;
    }

    // Measure execution time
    clock_t start = clock();

    // Find maximum and minimum elements
    max = arr[0];
    min = arr[0];
    for (int i = 1; i < SIZE; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
        if (arr[i] < min) {
            min = arr[i];
        }
    }

    // Measure execution time
    clock_t end = clock();
    double elapsed = (double)(end - start) / CLOCKS_PER_SEC;

    printf("Maximum element: %d\n", max);
    printf("Minimum element: %d\n", min);
    printf("Execution time: %f seconds\n", elapsed);

    free(arr);
    return 0;
}