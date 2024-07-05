#include<stdio.h>
#include<cuda_runtime.h>


__global__ void add_arrays(int *c , const int  *a, const int *b , int size){
    int i=blockIdx.x*blockDim.x+threadIdx.x;
   
    if(i<size){
        c[i]=a[i]+b[i];
    }
}


int main(){
    const int size=90000;

    int a[size],b[size];

    for (int i =0;i<size;i++)
    {
         a[i]=i;
         b[i]=i;
    }

    int *d_c;

    //Allocate memory on the device for array c
    cudaMalloc((void**)&d_c,size * sizeof(int));

    //Copy arrays a and b to the device
    int *d_a,*d_b;

    cudaMalloc((void**)&d_a , size*sizeof(int));
    cudaMalloc((void**)&d_b , size*sizeof(int));
    
    cudaMemcpy(d_a,a,size * sizeof(int),cudaMemcpyHostToDevice);
    cudaMemcpy(d_b,b,size * sizeof(int),cudaMemcpyHostToDevice);

    int threadPerBlock=512;
    int blockPerGrid=(size+threadPerBlock-1)/threadPerBlock;
    // printf("Block per grid : %d \n",blockPerGrid);
   

    // Start timing GPU execution
    cudaEvent_t start, stop;
    cudaEventCreate(&start);
    cudaEventCreate(&stop);
    cudaEventRecord(start);


    add_arrays<<<blockPerGrid,threadPerBlock>>>(d_c,d_a,d_b,size);
    cudaDeviceSynchronize();


// Stop timing GPU execution
    cudaEventRecord(stop);
    cudaEventSynchronize(stop);
    float milliseconds = 0;
    cudaEventElapsedTime(&milliseconds, start, stop);
   
    //copy thre result back from the device
    int *c =(int*)malloc(size * sizeof(int));

    cudaMemcpy(c,d_c,size*sizeof(int),cudaMemcpyDeviceToHost);

    //print the reslult
    for (int i=0;i<size;i++){
        printf("%d).%d \n",i,c[i]);
    }

    printf("\n");

  
    // Print time taken by GPU
    printf("Time taken by GPU : %f milliseconds\n", milliseconds);
    //free me
    cudaFree(c);
    cudaFree(d_a);
    cudaFree(d_c);
    cudaFree(d_b);


}