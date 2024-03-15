// 2. Write a union to store multiple options to store exam code details.
#include <stdio.h>

union ExamCodeDetails {
    int examCode;
    char examGrade;
    float examMarks;
};

int main() {
    union ExamCodeDetails exam;

    // Store an integer value
    exam.examCode = 10;

    // Access and print the integer value
    printf("Integer value: %d\n", exam.examCode);

    // Store a float value
    exam.examMarks = 3.14;
        printf("Float value: %f\n", exam.examMarks);

    // Store a character value
    exam.examGrade = 'A';


    // Access and print the character value
    printf("Character value: %c\n", exam.examGrade);

    return 0;
}
