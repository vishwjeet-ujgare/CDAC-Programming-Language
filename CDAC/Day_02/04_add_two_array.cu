#include<stdio.h>

#include<cuda.h>

__global__ void add_arrays(int *c , const int  *a, const int *b , int size){
    int i=blockIdx.x*blockDim.x+threadIdx.x;

    if(i<size){
        c[i]=a[i]+b[i];
    }
}


int main(){
    const int size=5;

    int a[size]={1,2,3,4,5};
    int b[size]={1,2,3,4,5};
    int *d_c;

    //Allocate memory on the device for array c
    cudaMalloc((void**)&d_c,size * sizeof(int));

    //Copy arrays a and b to the device
    int *d_a,*d_b;

    cudaMalloc((void**)&d_a , size*sizeof(int));
    cudaMalloc((void**)&d_b , size*sizeof(int));
    
    cudaMemcpy(d_a,a,size * sizeof(int),cudaMemcpyHostToDevice);
    cudaMemcpy(d_b,b,size * sizeof(int),cudaMemcpyHostToDevice);


    add_arrays<<<2,4>>>(d_c,d_a,d_b,size);
    cudaDeviceSynchronize();

    //copy thre result back from the device

    int *c =(int*)malloc(5 * sizeof(int));
    cudaMemcpy(c,d_c,size*sizeof(int),cudaMemcpyDeviceToHost);

    //print the reslult
    for (int i=0;i<size;i++){
        printf("%d ",c[i]);
    }
    printf("\n");
    //free me
    cudaFree(c);
    cudaFree(d_a);
    cudaFree(d_c);
    cudaFree(d_b);


}