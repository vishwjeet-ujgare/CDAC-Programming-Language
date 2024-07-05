//finding maximum number of threads ans blocks on out GPU ...

#include<iostream>
#include<cuda_runtime.h>

int main(){
    int maxThreadsBlock,maxBlocks;

    cudaDeviceGetAttribute(&maxThreadsBlock,cudaDevAttrMaxThreadsPerBlock,0);
    cudaDeviceGetAttribute(&maxBlocks,cudaDevAttrMaxGridDimX,0);

    std::cout<<"Maximum Threads per Block: "<<maxThreadsBlock<<std::endl;
    std::cout<<"Maximum  Block: "<<maxBlocks<<std::endl;
    return 0 ;
    
}