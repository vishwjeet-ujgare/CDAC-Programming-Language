#include <stdio.h>

int main()
{
    int length = 0;
    char str[] = "abcd";

    while (str[length] != '\0')
    {
        length++;
    }

    printf("\nLength of %s is %d.\n", str, length);
    return 0;
}

// Remove Vowels from a string
// Defanging an IP Address
// Number of Words Found in Sentences
// Count a char in string
// Replace a char by another char in string
// Reverse
// Palindrome