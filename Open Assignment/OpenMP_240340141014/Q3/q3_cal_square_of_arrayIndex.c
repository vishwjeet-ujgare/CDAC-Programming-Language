#include <stdio.h>
#include <omp.h>

int main() {
    // Set the number of threads to 6
    omp_set_num_threads(6);

    // Declare an array of size 6
    int a[6];

    // Start OpenMP parallel region
    #pragma omp parallel for
    for (int i = 0; i < 6; i++) {
        // Calculate the square of the index for this iteration
        int square = i * i;

        // Store the result in the array
        a[i] = square;

        // Print the result for this iteration
        printf("a[%d] = %d\n", i, square);
    }

    return 0;
}
