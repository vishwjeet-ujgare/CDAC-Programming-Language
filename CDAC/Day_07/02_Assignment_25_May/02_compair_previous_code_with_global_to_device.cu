// Assignment (25 May):Dyanamic Parallelism - 
    // Maintain a copy of the original code. Modify the code to have the square functinality inside the doubleValue function itself . Have 10000000 elements , instead of 10 in both versions. Compare the performance of the two versions by adding timing code.

#include<cuda.h>
#include<stdio.h>

__global__ void doubleValues(int* data, int size){
    int i= blockIdx.x * blockDim.x + threadIdx.x;
    if(i<size){
        int value =data[i];
        data [i]=(value * value) * 2;
    }

}

int main(){
    //Allocate memory on host and device
    int size=10000000;

    int* data_host=new int[size];
    int* data_device;
    cudaMalloc(&data_device, size * sizeof(int));

    //Initialize data on host
    for (int i=0;i<size;++i){
        data_host[i]=i;
    }

    //Copy data to device
    cudaMemcpy(data_device,data_host,size * sizeof(int),cudaMemcpyHostToDevice);


  //Timing code
    float gpuElapsed=0.0;
    cudaEvent_t start,stop;

    cudaEventCreate(&start);
    cudaEventCreate(&stop);

    //launch kernel
    int threadsPerBlock=256;

    //Record start time
    cudaEventRecord(start);
    doubleValues<<<(size + threadsPerBlock -1)/threadsPerBlock , threadsPerBlock>>>(data_device, size);

    //wait for kernel to finisj 
    cudaDeviceSynchronize();

    //record end time
    cudaEventRecord(stop);
        cudaEventSynchronize(stop);
    cudaEventElapsedTime(&gpuElapsed,start,stop);


    //copy data back from device
    cudaMemcpy(data_host,data_device,size * sizeof(int),cudaMemcpyDeviceToHost);

    //print results
    for (int i =0;i<size;++i){
        // printf("data[%d]=%d\n", i , data_host[i]);
    }

    //printing time 
    printf("GPU Processing time : %0.10f ms\n",gpuElapsed);

    //Free memory
    cudaFree(data_device);
    delete[] data_host;

    return 0;

}