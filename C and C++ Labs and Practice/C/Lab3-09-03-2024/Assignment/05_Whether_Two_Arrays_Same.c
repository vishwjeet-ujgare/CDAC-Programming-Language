#include <stdio.h>

#define MAX_SIZE 100

int main() {
    int nums[MAX_SIZE], size;

    // Input the size of the array
    printf("Enter the size of the array: ");
    scanf("%d", &size);

    // Input elements of the array
    printf("Enter %d elements: ", size);
    for (int i = 0; i < size; i++) {
        scanf("%d", &nums[i]);
    }

    // Compute running sum
    int running_sum = 0;
    printf("Running sum: ");
    for (int i = 0; i < size; i++) {
        running_sum += nums[i];
        printf("%d ", running_sum);
    }

    return 0;
}
