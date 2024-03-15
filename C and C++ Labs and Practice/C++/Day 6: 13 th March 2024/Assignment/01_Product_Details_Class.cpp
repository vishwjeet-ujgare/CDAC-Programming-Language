// 1. Write a class to store details of products like id, name and price.

#include <iostream>
#include<string.h>
using namespace std;

class Product{
public:

int id ;
string name ;
float price;

void displayProductDetails()
{
    cout<<"ID : "<<id<<endl;
    cout<<"Name :"<<name<<endl;
    cout<<"Price :"<<price<<endl;
}



};


int main()
{
    Product p;
    cout<<endl;
    p.id=1;
    p.name="Jeet";
    p.price=25555.60;

    cout<<"Product Details are "<<endl;
    p.displayProductDetails();
    
}