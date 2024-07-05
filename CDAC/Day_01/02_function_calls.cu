#include<cuda_runtime.h>
#include<stdio.h>

__global__ void kernal(void){

    printf("Hello from GPU\n");

}


void cpu_print(void){
    printf("Hello from CPU\n");
}


int main(){

    kernal <<<1,1>>>();
    kernal <<<1,1>>>();
    kernal <<<1,1>>>();
//ones cpu done there work it terminated and does not wait for GPU work do be completed

    cpu_print();
    cpu_print();
    cpu_print();

    return 0;
}