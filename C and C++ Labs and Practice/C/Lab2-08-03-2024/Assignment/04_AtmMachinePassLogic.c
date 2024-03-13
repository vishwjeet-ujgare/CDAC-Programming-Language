#include <stdio.h>

int main()
{
    int pin = 0, flag = -1, count = 0;

    do
    {
        if (count == 3)
        {
            printf("\nMax Attempts Reached: %d\n", count);
            break;
        }

        printf("\nEnter Pin:\n");
        scanf("%d", &pin);

        if (pin == 1234)
        {
            flag = 0;
            printf("\nWelcome To Bank ATM\n");
            printf("\n=====MENU=====\n");
            break;
        }

        else
        {
            flag = 1;
            count++;
            printf("\nInvalid Pin\n");
            printf("\nAttempts: %d\n", count);
        }
    } while (flag == 1);

    return 0;
}