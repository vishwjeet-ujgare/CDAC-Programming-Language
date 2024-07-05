#include "cuda_runtime.h"
// Includes necessary headers for CUDA functionalities

#include "device_launch_parameters.h"
// Might be specific to your development environment, include if needed

#include <stdio.h>
// Includes standard input/output library for printing

int main() {
    const int arraySize = 5;
    // Declares a constant integer variable to define array size (fixed size)

    // Host (CPU) data
    float hostArray[arraySize] = {1.0, 2.0, 3.0, 4.0, 5.0};
    // Initializes a float array on the host (CPU) with sample values

    float resultArray[arraySize];
    // Declares another float array on the host (CPU) to store copied data

    // Device (GPU) data
    float *deviceArray;
    // Declares a pointer to a float variable on the device (GPU)

    // Allocate memory on the device (GPU)
    cudaMalloc((void**)&deviceArray, arraySize * sizeof(float));
    // Allocates memory on the device (GPU) to hold the array data
    // Casts the result to a void pointer and stores the address in deviceArray

    // Copy data from CPU to GPU
    cudaMemcpy(deviceArray, hostArray, arraySize * sizeof(float), cudaMemcpyHostToDevice);
    // Copies the data from hostArray (CPU) to deviceArray (GPU)
    // cudaMemcpy arguments: destination, source, size, transfer direction

    // Copy data from GPU to CPU (redundant in this example)
    // cudaMemcpy(resultArray, deviceArray, arraySize * sizeof(float), cudaMemcpyDeviceToHost);
    // This line is commented out because the original hostArray is already overwritten

    // Display original array on host (CPU)
    printf("Original Array: ");
    for (int i = 0; i < arraySize; i++) {
        printf("%f, ", hostArray[i]);
    }
    printf("\n");

    // Process data on the GPU (replace with your GPU-specific computations)
    // This section is typically where you would launch a CUDA kernel to perform
    // computations on the GPU using the data on the device. Since this is a basic
    // example, we'll leave it empty.

    // **Optional:** Copy data back from GPU to CPU (if needed)
    // cudaMemcpy(resultArray, deviceArray, arraySize * sizeof(float), cudaMemcpyDeviceToHost);
    // Uncomment this line if you need the processed data back on the CPU

    // Free allocated memory on GPU
    cudaFree(deviceArray);
    // Frees the memory allocated on the device (GPU) to prevent memory leaks

    return 0;
}
