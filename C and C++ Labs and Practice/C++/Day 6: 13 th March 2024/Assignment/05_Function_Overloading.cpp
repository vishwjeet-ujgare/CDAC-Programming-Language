// 5. Demonstrate the concept of function overloading using area function
// which finds area of circle and square. (Assume float radius for circle and
// int side for square)

#include <iostream>

using namespace std;

const float PI = 3.14;

float area(float radius) {
    return PI * radius * radius; 
}

int area(int side) {
    return side * side; 
}

int main() {
    float radius;
    int side;

    cout << "Enter the radius of the circle: ";
    cin >> radius;
    cout << "Area of the circle: " << area(radius) << endl;

    cout << "Enter the side length of the square: ";
    cin >> side;
    cout << "Area of the square: " << area(side) << endl;

    return 0;
}


