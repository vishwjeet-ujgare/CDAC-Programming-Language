#include <cuda_runtime.h>
#include <stdio.h>
#include <stdlib.h>

// #define SIZE 10000000
#define SIZE 1000

#define BLOCK_SIZE 1024

__global__ void findMaxMinKernel(int *arr, int *max, int *min) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx >= SIZE) return;

    __shared__ int tempMax, tempMin;

    tempMax = arr[idx];
    tempMin = arr[idx];

    __syncthreads();

    for (int i = 1; i < blockDim.x; i *= 2) {
        if (threadIdx.x + i < blockDim.x) {
            if (arr[idx + i] > tempMax) {
                tempMax = arr[idx + i];
            }
            if (arr[idx + i] < tempMin) {
                tempMin = arr[idx + i];
            }
        }
        __syncthreads();
    }

    if (threadIdx.x == 0) {
        atomicMax(max, tempMax);
        atomicMin(min, tempMin);
    }
}

int main() {
    int *arr, *d_arr, *d_max, *d_min;
    int h_max, h_min;

    // Allocate memory on host and device
    arr = (int *)malloc(SIZE * sizeof(int));
    cudaMalloc((void **)&d_arr, SIZE * sizeof(int));
    cudaMalloc((void **)&d_max, sizeof(int));
    cudaMalloc((void **)&d_min, sizeof(int));

    // Initialize array with random values
    for (int i = 0; i < SIZE; i++) {
        arr[i] = rand() % 100;
    }

    // Copy array to device
    cudaMemcpy(d_arr, arr, SIZE * sizeof(int), cudaMemcpyHostToDevice);

    // Measure execution time
    cudaEvent_t start, stop;
    cudaEventCreate(&start);
    cudaEventCreate(&stop);
    cudaEventRecord(start, 0);

    // Launch kernel
    int numBlocks = (SIZE + BLOCK_SIZE - 1) / BLOCK_SIZE;
    findMaxMinKernel<<<numBlocks, BLOCK_SIZE>>>(d_arr, d_max, d_min);

    // Synchronize threads
    cudaDeviceSynchronize();

    // Measure execution time
    cudaEventRecord(stop, 0);
    cudaEventSynchronize(stop);
    float elapsed;
    cudaEventElapsedTime(&elapsed, start, stop);

    // Copy result back to host
    cudaMemcpy(&h_max, d_max, sizeof(int), cudaMemcpyDeviceToHost);
    cudaMemcpy(&h_min, d_min, sizeof(int), cudaMemcpyDeviceToHost);

    printf("Maximum element: %d\n", h_max);
    printf("Minimum element: %d\n", h_min);
    printf("Execution time: %f milliseconds\n", elapsed);

    // Free memory
    free(arr);
    cudaFree(d_arr);
    cudaFree(d_max);
    cudaFree(d_min);

    return 0;
}











