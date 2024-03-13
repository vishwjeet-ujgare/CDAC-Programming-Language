#include <stdio.h>


void replaceChar(char *str, char oldChar, char newChar) {
    while (*str != '\0') {
        if (*str == oldChar) {
            *str = newChar;
        }
        str++;
    }
}

int main() {
    char str[100];
    char oldChar, newChar;

   
    printf("Enter a string: ");
    scanf("%s", str);

    printf("Enter the old character: ");
    scanf(" %c", &oldChar); 

    printf("Enter the new character: ");
    scanf(" %c", &newChar); 

  
    replaceChar(str, oldChar, newChar);

    printf("Modified string: %s\n", str);

    return 0;
}