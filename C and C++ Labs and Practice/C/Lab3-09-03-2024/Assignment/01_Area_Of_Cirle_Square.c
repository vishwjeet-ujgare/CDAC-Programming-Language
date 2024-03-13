#include <stdio.h>

// Function to calculate area of a circle
float areaOfCircle(float radius) {
    return 3.14159 * radius * radius;
}

// Function to calculate area of a square
float areaOfSquare(float side) {
    return side * side;
}

int main() {
    float radius, side;

   
    printf("Enter the radius of the circle: ");
    scanf("%f", &radius);

    printf("Area of the circle: %.2f\n", areaOfCircle(radius));

    printf("Enter the side of the square: ");
    scanf("%f", &side);

    printf("Area of the square: %.2f\n", areaOfSquare(side));

    return 0;
}