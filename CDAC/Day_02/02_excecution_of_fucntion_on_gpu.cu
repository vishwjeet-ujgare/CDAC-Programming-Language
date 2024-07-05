#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>


//CUDA kernel to add two integers
__global__ void addIntegers(int* a ,  int* b , int* result){
    *result =*a+*b;
    printf("In GPU ... Sum id %d\n",*result);
}

int main(){
    //Host variables
    int host_a=5;
    int host_b=7;
    int host_result=0;//12

    //Declare for Device variables
    int *device_a;
    int *device_b;
    int *device_result;

    //Allocate memory on the device/host
    cudaMalloc((void**)&device_a,sizeof(int));
    cudaMalloc((void**)&device_b,sizeof(int));
    cudaMalloc((void**)&device_result,sizeof(int));

    //copy data from host to device
    cudaMemcpy(device_a,&host_a,sizeof(int),cudaMemcpyHostToDevice);
    cudaMemcpy(device_b,&host_b,sizeof(int),cudaMemcpyHostToDevice);

    //launch the kernel with one block and one head
    
    addIntegers <<<1,1>>>(device_a,device_b,device_result);
    // addIntegers <<<1,5>>>(device_a,device_b,device_result);
    // addIntegers <<<5,5>>>(device_a,device_b,device_result);
    // addIntegers <<<1,1025>>>(device_a,device_b,device_result);

    //1 block containers at most 1024
    // addIntegers <<<1,1024>>>(device_a,device_b,device_result);

    //copy the result from device to host
    cudaMemcpy(&host_result,device_result,sizeof(int),cudaMemcpyDeviceToHost);

    //Display the result
    printf("Sum of %d and %d is %d\n",host_a,host_b, host_result);

    //free alloacted memory
    cudaFree(device_a);
    cudaFree(device_b);
    cudaFree(device_result);
   
    return 0;



}