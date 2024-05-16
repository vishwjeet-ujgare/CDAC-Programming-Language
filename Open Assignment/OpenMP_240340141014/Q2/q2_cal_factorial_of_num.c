#include <stdio.h>
#include <omp.h>

// Function to calculate the factorial of a number using recursion
long long int factorial(int n) {
    if (n == 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

int main() {
    // Set the number of threads to 4
    omp_set_num_threads(4);

    // Set the value of the number to calculate the factorial of
    int num = 10;

    // Start OpenMP parallel region
    #pragma omp parallel
    {
        // Get the thread ID and the total number of threads
        int thread_id = omp_get_thread_num();
        int num_threads = omp_get_num_threads();

        // Calculate the partial factorial for this thread
        long long int partial_fact = factorial(num / num_threads * thread_id);

        // Wait for all threads to finish before continuing
        #pragma omp barrier

        // Calculate the total factorial using a reduction clause
        #pragma omp atomic
        num_threads *= partial_fact;
    }

    // Print the total factorial
    printf("Factorial of %d is: %lld\n", num, factorial(num));

    return 0;
}
