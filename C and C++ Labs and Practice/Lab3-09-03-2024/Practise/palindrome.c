#include <stdio.h>
int main()
{
    int i = 0, j = 0, l = 0, mid = 0;
    i = 0;
    l = 5;
    mid = l / 2;
    j = l - 1;
    char str[] = "nitin";

    while (i < j)
    {
        if (str[i] != str[j])
            break;

        else
        {
            i++;
            j--;
        }
    }

    if (i == j)
        printf("String is Palindrome.");

    else
        printf("String is not Palindrome.");

    return 0;
}