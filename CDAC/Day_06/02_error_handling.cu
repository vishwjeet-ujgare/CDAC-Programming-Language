#include "cuda_runtime.h"
#include "device_launch_parameters.h"

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//CUDA kernel to add two arrays element-wise with more thread details

__global__ void addArrays(const int* a, const int* b, int* result, int size){
    int idx = blockIdx.x * blockDim.x + threadIdx.x;


    //thread details
    int blockId = blockIdx.x;
    int threadId = threadIdx.x;

    //int threadsPerBlock = blockDim.x;
    int totalThreads = blockDim.x * gridDim.x;

    //check if the thread index is withim the valid range
    if(idx < size){
        printf("Thread %d (Block %d, Thread in Block %d, Total Thread %d): Adding %d + %d = %d\n", idx, blockId, threadId, totalThreads, a[idx], b[idx], a[idx] + b[idx]);
        result[idx] = a[idx] + b[idx];

    
    }
}
int main(){
    const int arraySize = 100;

    //Host (CPU) data
    int hostArray1[arraySize];
    int hostArray2[arraySize];
    int hostResultArray[arraySize];

    //Generate random integer numbers for the host arrays
    srand((unsigned)time(NULL));
    for(int i = 0; i < arraySize; i++){
        hostArray1[i]= rand() %100; //Random number between 0 to 99
        hostArray2[i]= rand() %100; //Random number between 0 to 99
    }

    //Device (GPU) data
    int* deviceArray1;
    int* deviceArray2;
    int* deviceResultArray;

    //Allocate device memory
    cudaError_t cudaStatus;

    // cudaStatus = cudaMalloc((void**)&deviceArray1, arraySize * sizeof(int));
    cudaStatus = cudaMalloc((void**)&deviceArray1, 0);//error will occure
    if (cudaStatus != cudaSuccess){
        fprintf(stderr, "cudaMalloc for deviceArray1 failed : %s\n", cudaGetErrorString(cudaStatus));
        exit(EXIT_FAILURE);

    }
    cudaStatus = cudaMalloc((void**)&deviceArray2, arraySize * sizeof(int));
    if (cudaStatus != cudaSuccess){
        fprintf(stderr, "cudaMalloc for deviceArray2 failed : %s\n", cudaGetErrorString(cudaStatus));
        exit(EXIT_FAILURE);
    }
    cudaStatus = cudaMalloc((void**)&deviceResultArray, arraySize * sizeof(int));
    if (cudaStatus != cudaSuccess){
        fprintf(stderr, "cudaMalloc for deviceResultArray failed : %s\n", cudaGetErrorString(cudaStatus));
        cudaFree(deviceArray1);
        cudaFree(deviceArray2);
        exit(EXIT_FAILURE);
    }

    //copy data from cpu to gpu
    // on purpose
    /*
    cudaStatus = cudaMemcpy(deviceArray1, hostArray1, arraySize * sizeof(int),cudaMemcpyHostToDevice);
    if (cudaStatus != cudaSuccess){
        fprintf(stderr, "cudaMemcpy (host to device) for deviceArray1 failed : %s\n", cudaGetErrorString(cudaStatus));
        cudaFree(deviceArray1);
        cudaFree(deviceArray2);
        cudaFree(deviceResultArray);
        exit(EXIT_FAILURE);
    }

    */
   //checking for error
        cudaStatus = cudaMemcpy(deviceArray1, hostArray1, arraySize * sizeof(int),cudaMemcpyHostToDevice);

     cudaStatus = cudaMemcpy(deviceArray2, hostArray2,  arraySize *  sizeof(int),cudaMemcpyHostToDevice);
     if (cudaStatus != cudaSuccess){
        fprintf(stderr, "cudaMemcpy (host to device) for deviceArray2 failed : %s\n", cudaGetErrorString(cudaStatus));
        cudaFree(deviceArray1);
        cudaFree(deviceArray2);
        cudaFree(deviceResultArray);
        exit(EXIT_FAILURE);
    }

    //Launce the kernel to add arrays on the device
    addArrays <<<1, arraySize >>>(deviceArray1, deviceArray2, deviceResultArray, arraySize);

    //Synchronize to ensure kernel execution is completed before proceeding
    cudaStatus = cudaDeviceSynchronize();
    if (cudaStatus != cudaSuccess){
        fprintf(stderr, "cudaDeviceSynchronize failed : %s\n", cudaGetErrorString(cudaStatus));
        cudaFree(deviceArray1);
        cudaFree(deviceArray2);
        cudaFree(deviceResultArray);
        exit(EXIT_FAILURE);
    }

    //copy the result data from GPU to CPU
    cudaStatus = cudaMemcpy(hostResultArray, deviceResultArray, arraySize * sizeof(int), cudaMemcpyDeviceToHost);
    if (cudaStatus != cudaSuccess){
        fprintf(stderr, "cudaMemcpy (device to host) for hostResultArray failed : %s\n", cudaGetErrorString(cudaStatus));
        cudaFree(deviceArray1);
        cudaFree(deviceArray2);
        cudaFree(deviceResultArray);
        exit(EXIT_FAILURE);
    }

    //Display results
    printf("Array 1 : ");
    for(int i = 0; i < arraySize; i++){
        printf("%d ", hostArray1[i]);

    }
    printf("\n");
    printf("Array 2 : ");
    for(int i = 0; i < arraySize; i++){
        printf("%d ", hostArray2[i]);
    }
    printf("\n");

    printf("Result Array : ");
    for(int i = 0; i < arraySize; i++){
        printf("%d ", hostResultArray[i]);
    }
    printf("\n");

    //Free allocateed memory on GPU
    cudaFree(deviceArray1);
    cudaFree(deviceArray2);
    cudaFree(deviceResultArray);

    return 0;
}