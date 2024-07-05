// 2 From original copy of the code , create a new code file.
// Try to make the squre funtion also global , instead of it being a device function. Try to execute and note your observations

#include<cuda.h>
#include<stdio.h>

// Include the square function header


#include<cuda_runtime.h>


__global__ void square(int *a){
  
     int num=*a;
     *a=num*num;
   
    // printf("Thread(%d,%d) -  squaring values \n",blockIdx.x,threadIdx.x);
    // printf("%d\n",*a);

}


__global__ void doubleValues(int* data, int size){
    int i= blockIdx.x * blockDim.x + threadIdx.x;
    if(i<size){
        
        int* value=data+i;
        //call square function and print thread ID
        square<<<1,1>>>(value);
        cudaDeviceSynchronize();//wait for the parent to complete

        // printf("Thread (%d , %d )-doubling squared value \n",blockIdx.x,threadIdx.x);
        int doubleOfSquare=(*value)*2;
      printf("%d \n",doubleOfSquare);
    }

}

int main(){
    //Allocate memory on host and device
    int size=10;

    int* data_host=new int[size];
    int* data_device;

    cudaMalloc(&data_device, size * sizeof(int));

    //Initialize data on host
    for (int i=0;i<size;++i){
        data_host[i]=i;
    }

    //Copy data to device
    cudaMemcpy(data_device,data_host,size * sizeof(int),cudaMemcpyHostToDevice);

    //Time code
    float gpuElapsed=0.0;
    cudaEvent_t start,stop;

    cudaEventCreate(&start);
    cudaEventCreate(&stop);

    //launch kernel
    int threadsPerBlock=256;

    cudaEventRecord(start);
    doubleValues<<<(size + threadsPerBlock -1)/threadsPerBlock , threadsPerBlock>>>(data_device, size);

    //wait for kernel to finisj 
    cudaDeviceSynchronize();


    //Record end time
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