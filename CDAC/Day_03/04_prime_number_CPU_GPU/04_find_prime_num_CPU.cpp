/*
part 1
Write a CPU program to find which number between 2 to 100001 are prime.
Display all such numbers and time the code.
*/


#include <iostream>
#include <chrono>

bool isPrimeNum(int num);

int main() {
    int fromNum = 2;
    int toNum = 2000001;

    // Record the start time
    auto start_time = std::chrono::high_resolution_clock::now();

       // process that we have calculate
    for (int i = fromNum; i < toNum; i++) {
        if (isPrimeNum(i)) {
            // std::cout << i << ", ";8
            
        }
    }

      // Record the end time
    auto end_time = std::chrono::high_resolution_clock::now();
    
    // Calculate duration
    auto duration_ns = std::chrono::duration_cast<std::chrono::nanoseconds>(end_time - start_time).count();

    double milliseconds = duration_ns / 1000000.0; // Convert nanoseconds to milliseconds

    std::cout << "Time taken by CPU: " << milliseconds << " milliseconds" << std::endl;
    return 0;
}

bool isPrimeNum(int num) {
    if (num <= 1) {
        return false;
    }
    if (num <= 3) {
        return true;
    }
    
   
    for (int i = 2; i <num; i ++) {
        if (num % i == 0 ) {
            return false;
        }
    }

    return true;
}



