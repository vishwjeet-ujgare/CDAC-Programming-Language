#include <stdio.h>
int main()
{
    int i = 0, j = 0;
    char a[5];
    char b[5];
    char c[10];
    printf("Enter string a: ");
    scanf("%s", a);
    printf("Enter string b: ");
    scanf("%s", b);

    for (i = 0, j = 4; i < 4; i++, j++)
    {
        c[i] = a[i];
        c[j] = b[i];
    }

    c[8] = '\0';

    printf("%s", c);

    return 0;
}