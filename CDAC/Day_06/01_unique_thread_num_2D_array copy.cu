#include <stdio.h>
#include <cuda.h>
#include <cuda_runtime.h>

#define M 4  
#define N 5  

__global__ void addArrays2D(int* d_result, int* d_array1, int* d_array2,int totalBlock) {
  int blockIdxX = blockIdx.x;
  int blockIdxY = blockIdx.y;
  int threadIdxX = threadIdx.x;
  int threadIdxY = threadIdx.y;

  int row = blockIdxY * blockDim.y + threadIdxY;
  int col = blockIdxX * blockDim.x + threadIdxX;

  int tId=row*totalBlock+col;
  // Check for valid element within array bounds
  if (row < M && col < N) {
    // int result = d_array1[row * N + col] + d_array2[row * N + col];
    // d_result[row * N + col] = result;
    printf("unique thread number = %d \n",tId);
  }
}

int main() {
  // Host memory for the arrays
  int host_array1[M][N] = {
    {1, 2, 3, 4, 5},
    {6, 7, 8, 9, 10},
    {11, 12, 13, 14, 15},
    {16, 17, 18, 19, 20}
  };
  int host_array2[M][N] = {
    {10, 20, 30, 40, 50},
    {60, 70, 80, 90, 100},
    {110, 120, 130, 140, 150},
    {160, 170, 180, 190, 200}
  };

  // Allocate memory on device for the arrays
  int* d_array1, *d_array2, *d_result;
  cudaMalloc(&d_array1, M * N * sizeof(int));
  cudaMalloc(&d_array2, M * N * sizeof(int));
  cudaMalloc(&d_result, M * N * sizeof(int));

  // Copy arrays from host to device
  cudaMemcpy(d_array1, host_array1, M * N * sizeof(int), cudaMemcpyHostToDevice);
  cudaMemcpy(d_array2, host_array2, M * N * sizeof(int), cudaMemcpyHostToDevice);

  // Define grid and block sizes
  int threadsPerBlockX = 16;
  int threadsPerBlockY = 4;
  dim3 threadsPerBlock(threadsPerBlockX, threadsPerBlockY, 1);
  int numBlocksX = (N + threadsPerBlockX - 1) / threadsPerBlockX;
  int numBlocksY = (M + threadsPerBlockY - 1) / threadsPerBlockY;
  dim3 blocksPerGrid(numBlocksX, numBlocksY, 1);

  int totalBlock=numBlocksX*numBlocksY;

  // Launch the kernel
  addArrays2D<<<blocksPerGrid, threadsPerBlock>>>(d_result, d_array1, d_array2,totalBlock);

  // Allocate memory on host to store results
  int host_result[M][N];

  // Copy results back from device to host
  cudaMemcpy(host_result, d_result, M * N * sizeof(int), cudaMemcpyDeviceToHost);

  // Print the result array
  printf("Resulting Array:\n");
  for (int i = 0; i < M; ++i) {
    for (int j = 0; j < N; ++j) {
      printf("%d ", host_result[i][j]);
    }
    printf("\n");
  }

  // Free memory on device
  cudaFree(d_array1);
  cudaFree(d_array2);
  cudaFree(d_result);

  return 0;
}