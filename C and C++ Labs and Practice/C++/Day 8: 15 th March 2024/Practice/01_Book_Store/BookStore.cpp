#include <iostream>
#include <string>
using namespace std;

class BookStore
{
private:
    int id;
    string author;
    string title;
    string publisher;
    float price;
    int stock;

public:
    BookStore()
    {
    }

    BookStore(int id,
              string author,
              string title,
              string publisher,
              float price,
              int stock)
    {
        this->id = id;
        this->author = author;
        this->title = title;
        this->publisher = publisher;
        this->price = price;
        this->stock = stock;
    }

    // getter setter for id
    int GetId() const
    {
        return id;
    }

    void SetId(int id)
    {
        id = id;
    }

    // getter setter for author

    string GetAuthor() const
    {
        return author;
    }

    void SetAuthor(string author)
    {
        author = author;
    }

    // getter setter for title
    string GetTitle() const
    {
        return title;
    }

    void SetTitle(string title)
    {
        title = title;
    }

    // getter setter for Publisher
    string GetPublisher() const
    {
        return publisher;
    }

    void SetPublisher(string publisher)
    {
        publisher = publisher;
    }

    // getter setter for price

    float GetPrice() const
    {
        return price;
    }

    void SetPrice(float price)
    {
        price = price;
    }

    // getter setter for stock
    int GetStock() const
    {
        return stock;
    }

    void SetStock(int stock)
    {
        stock = stock;
    }

    void printBook()
    {
        cout << "--------------------------" << endl;
        cout << "Id :" << id << endl;
        cout << "Author :" << author << endl;
        cout << "Title :" << title << endl;
        cout << "Publisher :" << publisher << endl;
        cout << "Stock :" << stock << endl;
    }
};

int main()
{
    BookStore books[5] = {
        BookStore(101, "E. Balagurusamy", "C++ Guide", "Packt", 848.3, 43),
        BookStore(454, "Willliam Stallings", "C++ Guide", "Packt", 848.3, 43),
        BookStore(545, "E. Balagurusamy", "Operating Systems", "Tata McGraw-Hill", 432.3, 44),
        BookStore(646, "Ron Patton", "Software Testing", "Wordpress", 2122.3, 22),
        BookStore(707, "Rahul Joshi", "Design Pattern", "ata McGraw-Hill", 848.3, 98)};

    int id;
    int stock;
    bool isBookFound = false;
    ;

    cout << "Enter book id : ";
    cin >> id;

    cout << "Enter order stock : ";
    cin >> stock;

    // cout<<"Enter detail are "<<id<<" "<<stock;
    for (int i = 0; i < 5; i++)
    {
        if (books[i].GetId() == id)
        {
            isBookFound = true;
            int remainStock = books[i].GetStock() - stock;

            if (remainStock >= 0)
            {
                books[i].SetStock(remainStock);
                cout << "Congratualation your order has placed !" << endl;
            }
            else
            {
                cout << "Required copies are not in stock." << endl;
            }
            break;
        }
        else
        {

            isBookFound = false;
        }
    }


    if(!isBookFound)
    {
        cout << "Required Book was not found in stock." << endl; 
    }
}