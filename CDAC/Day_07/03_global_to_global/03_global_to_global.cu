#include<stdio.h>
#include<cuda.h>

__global__ void childKernel(){
    printf("Hello from child kernel function\n");
}


__global__ void parentKernel(){
    childKernel<<<1,1>>>();
    cudaDeviceSynchronize();//wair for the child to comple
    printf("Hello from parent kernel function\n");
}

int main(){
    parentKernel<<<1,1>>>();
    cudaDeviceSynchronize();//wait for the parent to complete

    return 0;
}

// nvcc 03_global_to_global.cu -rdc=true-