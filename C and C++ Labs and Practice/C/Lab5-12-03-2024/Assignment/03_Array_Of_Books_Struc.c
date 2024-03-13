#include <stdio.h>

struct Book{
    int id;
    char name[20];
    float price;
};

void displayBookDetails(struct Book b)
{
    // printf("\n\n------Entered Book Details Are-------\n");
    printf("\n         Book Id : %d", b.id);
    printf("\nEnter book name  : %s", b.name);
    printf("\nEnter book price : %f", b.price);
}

void displayAllBooks(struct Book booksArray[], int bookCount)
{
    printf("\n------All Book Details Are-------\n");
    for (int i = 0; i < bookCount; i++)
    {
        printf("\n------Book %d-------", i + 1);
        displayBookDetails(booksArray[i]);
    }
}

struct Book takeBookDetails(int id)
{
    struct Book b;
    b.id = id;

    printf("\n\nBook Id will be : %d", id);

    printf("\nEnter book name : ");
    scanf("%s", b.name);

    printf("Enter book price : ");
    scanf("%f", &b.price);
 
    return b;
}

int main()
{
    int bookCount = 0;
    int count = 0;

    printf("\n\n How many book details you want to add : ");
    scanf("%d", &bookCount);

    struct Book booksArray[bookCount]; // Declare booksArray after taking bookCount

    printf("\n\n------Enter a book details--------\n");

    while (count < bookCount)
    {
        struct Book b;
        b = takeBookDetails(count + 1);
        booksArray[count] = b;
        count++;
        //    displayBookDetails(b);
    }

    displayAllBooks(booksArray, bookCount);

    printf("loop is ended");

    return 0;
}
