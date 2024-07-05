// write a c++ program to implement selection sort algorithm
#include <iostream>
using namespace std;

// function for selcting and swapping  elements in array
void selectionSort(int arr[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        int minIndex = i;
        for (int j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[minIndex])
            {
                minIndex = j;
            }
        }
        swap(arr[i], arr[minIndex]);
    }
}

// printing sorted array
void printArray(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

// main method
int main()
{

    int arr[] = {5, 41, 12, 4, 2};

    int n = sizeof(arr) / sizeof(arr[0]);

    selectionSort(arr, n);

    cout << "\n\n Printing Sorted array: \n";
    printArray(arr, n);

     cout << "\n\n \n";

    return 0;
}