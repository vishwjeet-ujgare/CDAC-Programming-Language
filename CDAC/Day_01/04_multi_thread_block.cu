#include<stdio.h>
#include<cuda_runtime.h>

__global__ void kernel(void){
    printf("Hello from GPU\n");
}

void cpu_print(void)
{
    printf("Hello form CPU\n");
}

int main()
{
    // kernel <<<1,1>>>();
    // kernel <<<1,10>>>();
    kernel <<<2,2>>>();
    
    cudaDeviceSynchronize();

    printf("----------------\n");
    cpu_print();
    return 0;
}