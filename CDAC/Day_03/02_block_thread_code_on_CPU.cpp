#include <iostream>
#include <chrono>

#define SIZE 90000

void processArrays(const int *, const int *, int *);

int main() {
    int a[SIZE], b[SIZE], c[SIZE];

    for (int i = 0; i < SIZE; i++) {
        a[i] = i;
        b[i] = i;
    }

    // Record the start time
    auto start_time = std::chrono::high_resolution_clock::now();

    // processArrays(a, b, c);
    for (int i = 0; i < SIZE; i++) {
        c[i] = a[i] + b[i];
    }

    // Record the end time
    auto end_time = std::chrono::high_resolution_clock::now();

    // Calculate duration
    auto duration_ns = std::chrono::duration_cast<std::chrono::nanoseconds>(end_time - start_time).count();

    double milliseconds = duration_ns / 1000000.0; // Convert nanoseconds to milliseconds

    // // Print the results
    // for (int i = 0; i < SIZE; i++) {
    //     std::cout << i << "): " << c[i] << std::endl;
    // }

    std::cout << "Time taken by CPU: " << milliseconds << " milliseconds" << std::endl;

    return 0;
}

// void processArrays(const int *a, const int *b, int *c) {
//     for (int i = 0; i < SIZE; i++) {
//         c[i] = a[i] + b[i];
//     }
// }


//to run this program compile using below 
// g++ -std=c++11 01_block_thread_code_on_CPU.cpp

// run using 
./a.out