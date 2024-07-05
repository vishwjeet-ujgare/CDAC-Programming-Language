#include<cuda_runtime.h>
#include "device_launch_parameters.h"
#include<stab.h>
#include <stdio.h>
#include <iostream>

__global__ void printValue(int* data){
    int tid=threadIdx.x+blockIdx.x * blockDim.x;

    //Access managed memory directly from the GPU
    printf("GPU THread %d : value = %d \n",tid,data[tid]);
}

int main(){

    const int N =10;

    //Allocate managed memory
    int* data;
    cudaMallocManaged(&data,N*sizeof(int));

    //Initialize data on the CPU
    for (int i =0;i<N;++i){
        data[i]=i*2;
    }

    //Launch GPU kernel to print values
    printValue<<<1,N>>>(data);
    cudaDeviceSynchronize();//Ensure GPU kernel completes

    //Access managed directly from the CPU
    for(int i=0;i<N;++i){
        printf("CPU : value = %d \n",data[i]);
    }

    //Free managed memory 
    cudaFree(data);

    return 0;
}