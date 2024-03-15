// 1. Overload an operator ‘+’ which increases the length and width of box variable.
#include<iostream>
using namespace  std;

class Reactangle
{
public:
    int l,w;

public:
 Reactangle()
{
    l=10;
    w=20;
}

void operator++()
    {
         l++;
         w++;
    }

void displayDetails(Reactangle r)
{
    cout<<"l : "<<r.l<<endl;
     cout<<"w : "<<r.w<<endl;
    
}

};

int main()
{
  Reactangle r;
  ++r;

r.displayDetails(r);

}