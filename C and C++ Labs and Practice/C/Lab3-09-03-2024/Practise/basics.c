#include <stdio.h>
int main()
{
    int i = 0;
    char name[5];
    printf("Enter name: ");
    scanf("%s", name);
    // printf("Your name is %s.", name);

    // display a string
    printf("Your name is: ");
    for (i = 0; i < 4; i++)
    {
        printf("%c", name[i]);
    }

    return 0;
}

// char c[] = "abcd";

// char c[50] = "abcd";

// char c[] = {'a', 'b', 'c', 'd', '\0'};

// char c[5] = {'a', 'b', 'c', 'd', '\0'};