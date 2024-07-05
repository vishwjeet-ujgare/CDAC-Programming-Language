#include "cuda_runtime.h"
#include "device_launch_parameters.h"

#include<stdio.h>

int main(){
    int deviceCount;

    cudaGetDeviceCount(&deviceCount);

    if(deviceCount==0){
        printf("No cuda device found.\n");
        return 1;
    }


    for (int device=0;device<deviceCount;++device){
        cudaDeviceProp deviceProp;
        cudaGetDeviceProperties(&deviceProp , device);


        printf("              Device %d : %s\n",device,deviceProp.name);
        printf("     Coputer Capability : %d.%d\n",deviceProp.major,deviceProp.minor);
        printf("    Total Global Memory : %lu\n",(unsigned long)deviceProp.totalGlobalMem);
        printf("Shared memory per BLock : %lu bytes\n",(unsigned long) deviceProp.sharedMemPerBlock);
        
        printf("              wrap Size : %d\n",deviceProp.warpSize);
        printf("  Max Threads Per Block : %d\n",deviceProp.maxThreadsPerBlock);
        printf(" Max Threads Diamension : (%d, %d,%d)\n",deviceProp.maxThreadsDim[0],deviceProp.maxThreadsDim[1],deviceProp.maxThreadsDim[2] );
        printf("          Max Grid Size : (%d, %d,%d)\n",deviceProp.maxThreadsDim[0],deviceProp.maxThreadsDim[1],deviceProp.maxGridSize[2]);

        printf("             Clock Rate : %d kHz\n",deviceProp.clockRate);
        printf("      Memory Clock Rate : %d kHz\n",deviceProp.memoryClockRate);
        printf("       Memory Bus width : %d bits\n",deviceProp.memoryBusWidth);
        printf("          L2 Cache size : %d bytes \n",deviceProp.l2CacheSize);
        printf("   Constant memory size : %lu bytyes \n",(unsigned long) deviceProp.totalConstMem);

        printf("      Texture Alignment : %lu bytyes \n",(unsigned long) deviceProp.textureAlignment);
        printf("\n");
       

    }
     return 0;
}