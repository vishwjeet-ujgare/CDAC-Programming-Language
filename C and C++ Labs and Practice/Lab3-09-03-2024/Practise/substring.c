#include <stdio.h>
int main()
{
    int start = 1;
    int end = 3;
    int i = 0;
    int j = 0;
    char str[] = "abcdefg";
    char sub[50] = "";

    for (i = 0, j = start; j < end; i++, j++)
    {
        sub[i] = str[j];
    }
    sub[i] = '\0';

    printf("\nString is: %s\n", str);
    printf("\nSub String is: %s\n", sub);

    return 0;
}