// Dummy "Bitcoin mining" - GPU code
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <cuda_runtime.h>
#include <device_launch_parameters.h>
#include <chrono>
#include <iostream>

#define TARGET_DIFFICULTY 1000000000

__device__ uint32_t calculateHash(uint32_t nonce) {
    return nonce; // Simplified hash calculation

}

__global__ void mineBitcoin(uint32_t* nonce) {
    // int tid = blockIdx.x * blockDim.x + threadIdx.x;
    uint32_t hash;
    do {
        hash = calculateHash(*nonce);
        (*nonce)++;
    }while (hash < TARGET_DIFFICULTY);
}

int main() {
    uint32_t* d_nonce;
    cudaMalloc(&d_nonce, sizeof(uint32_t));

    uint32_t initialNonce = 0;
    cudaMemcpy(d_nonce, &initialNonce, sizeof(uint32_t), cudaMemcpyHostToDevice);

    int threadsPerBlock = 1024;
    int numBlocks = (TARGET_DIFFICULTY + threadsPerBlock - 1) / threadsPerBlock;

    auto start_time = std::chrono::high_resolution_clock::now();
    mineBitcoin <<<numBlocks, threadsPerBlock>>> (d_nonce);
    auto end_time = std::chrono::high_resolution_clock::now();

    auto duration_ns = std::chrono::duration_cast<std::chrono::nanoseconds>(end_time - start_time).count();
    cudaDeviceSynchronize();
    std::cout<<"Time taken by GPU   : " << duration_ns << " nanoseconds"<< std::endl;

    cudaFree(d_nonce);
    return 0;
}