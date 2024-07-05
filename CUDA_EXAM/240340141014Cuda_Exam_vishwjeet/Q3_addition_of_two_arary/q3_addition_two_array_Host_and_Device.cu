#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <chrono>

__global__ void sumArraysOnGPU(float *A, float *B, float *C, const int N) {
    int tid = threadIdx.x + blockIdx.x * blockDim.x;
    if (tid < N)
        C[tid] = A[tid] + B[tid];
}



void initialData(float *giveArray, int size) {

// //randome float values
//     for (int i = 0; i < size; i++) {
//         giveArray[i] = (float)(rand() & 0xFF) / 10.0f;
//     }

//Or with the values of the irerator as per questions
for (int i = 0; i < size; i++) {
    giveArray[i] = i * 1.0; 
    // printf("%f \n", giveArray[i]);
    }

}

//Sequential additoin of two arrays
void sumArraysOnHost(float *A, float *B, float *C, const int N) {
    for (int idx = 0; idx < N; idx++)
        C[idx] = A[idx] + B[idx];
}

int main(int argc, char ** argv) {
    printf("%s Starting...\n", argv[0]);

    // seting up data size of array elements 
    int N = 1000000;

    printf("Array size %d\n", N);

    // allocating host  memory with size_t for N for float
    //to avoid repeatation of counting array size
    size_t nBytes = N * sizeof(float);

    // initializing  pointers or a references for strong gpu address
    float *h_A, *h_B, *hostRef, *gpuRef;

    //assigning memory on host with malloc
    h_A = (float *) malloc(nBytes);
    h_B = (float *) malloc(nBytes);
    hostRef = (float *) malloc(nBytes);
    gpuRef = (float *) malloc(nBytes);

    //Initilize array A and B with randome float numbers or integer as mentioned in the questions
    initialData(h_A, N);
    initialData(h_B, N);

   // sets a block of memory to a specified value. 

    memset(hostRef, 0, nBytes);
    memset(gpuRef, 0, nBytes);

    // Performing addition on Host and storing that in hostRef
    auto start_time = std::chrono::high_resolution_clock::now();
    sumArraysOnHost(h_A, h_B, hostRef, N);
    auto end_time = std::chrono::high_resolution_clock::now();


    //measurint time for cpu
    auto duration_ns = std::chrono::duration_cast < std::chrono::nanoseconds > (end_time - start_time).count();
    double seconds_cpu = duration_ns / 1000000000.0;
    std::cout << "Time taken by CPU : " << seconds_cpu << " seconds" << std::endl;


    //code for GPU

    // cudamalloc device global memory
    float *d_A, *d_B, *d_C;
    cudaMalloc((float **) &d_A, nBytes);
    cudaMalloc((float **) &d_B, nBytes);
    cudaMalloc((float **) &d_C, nBytes);

    // transfer data from host to device
    cudaMemcpy(d_A, h_A, nBytes, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B, nBytes, cudaMemcpyHostToDevice);

    // calling kernel funtion
    int threadsPerBlock = 1024;
    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;

    cudaEvent_t start, stop;
    cudaEventCreate(&start);
    cudaEventCreate(&stop);

    cudaEventRecord(start);
    sumArraysOnGPU<<<blocksPerGrid, threadsPerBlock>>>(d_A, d_B, d_C, N);
    cudaEventRecord(stop);
    cudaEventSynchronize(stop);

    float milliseconds_device=0 ;
    cudaEventElapsedTime(&milliseconds_device, start, stop);
    printf("Time taken by device(GPU): %f seconds\n", milliseconds_device/1000);

    // copy kernel result back to host side
    cudaMemcpy(gpuRef, d_C, nBytes, cudaMemcpyDeviceToHost);

    // free device global memory
    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);

    // free host memory
    free(h_A);
    free(h_B);
    free(hostRef);
    free(gpuRef);

    return 0;
}
