#include<stdio.h>
#include<stdio.h>
#include<cuda_runtime.h>

__global__ void vectorAddition_kernel(int* d_a,int* d_b,int* d_c,int N){
    int tid=threadIdx.x;
    int i;
    for(i = tid; i < N; i += blockDim.x){
        d_c[i]=d_a[i]+d_b[i];
        printf("TID :%d = %d \n",tid,d_c[i]);
    }
}


int main()
{

    // int N=8;
    int N=12;
    int* h_a,*h_b,*h_c;//host variables
    int* d_a,*d_b,*d_c;//Device variables

    //Allocate memory for host variables
    h_a=(int*)malloc(N * sizeof(int));
    h_b=(int*)malloc(N * sizeof(int));
    h_c=(int*)malloc(N * sizeof(int));


    //Allocate memory for device variables
    cudaMalloc((void**)&d_a,N*sizeof(int));
    cudaMalloc((void**)&d_b,N*sizeof(int));
    cudaMalloc((void**)&d_c,N*sizeof(int));

    //Initialize host variable
    for(int i=0;i<N;i++){
        h_a[i]=2;
        h_b[i]=2;
        h_c[i]=0;
    }

    //copy host variables to device
    cudaMemcpy(d_a,h_a,N * sizeof(int),cudaMemcpyHostToDevice);
    cudaMemcpy(d_b,h_b,N * sizeof(int),cudaMemcpyHostToDevice);

    //Launch kernel function
    int blockSize=1;
    // int numThreads=N;
    int numThreads=4;//to see what

    vectorAddition_kernel<<<blockSize,numThreads>>>(d_a,d_b,d_c,N);

    //copy result back to host
    cudaMemcpy(h_c,d_c,N * sizeof(int),cudaMemcpyDeviceToHost);

    //Display results
    printf("Result : ");

    for(int i=0;i<N;i++){
        printf("%d ",h_c[i]);
    }

    printf("\n");

     //free  device and host memory
    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);

    free(h_a);
    free(h_b);
    free(h_c);
    
}