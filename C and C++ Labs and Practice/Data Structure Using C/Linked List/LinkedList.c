#include <stdio.h>
#include <stdlib.h>

struct Node *head = NULL;
struct Node *tail = NULL;

struct Node
{
    int data;
    struct Node *next;
};

void addToStart(int data)
{
    struct Node *node = malloc(sizeof(struct Node));
    node->data = data;
    node->next = NULL;

    if (head == NULL)
    {
        head = node;
        tail = node;
        node->next = NULL;
    }
    else
    {
        node->next = head;
        head = node;
    }
}

void addEnd(int data)
{
    struct Node *node = malloc(sizeof(struct Node));
    node->data = data;

    if (head == NULL)
    {
        head = node;
        tail = node;
        node->next = NULL;
    }
    else
    {
        tail->next = node;
        tail = node;
    }
}

void addAfter(int data, int insertAfter)
{
    struct Node *node = malloc(sizeof(struct Node));
    node->data = data;
    struct Node *curr = head;

    while (curr != NULL)
    {

        if (curr->data == insertAfter)
        {
            if (curr == tail)
            {
                addEnd(data);
                return;
            }
            node->next = curr->next;
            curr->next = node;

            return;
        }
        else
        {
            curr = curr->next;
        }
    }
}

void addBefore(int data, int insertBefore)
{
    struct Node *node = malloc(sizeof(struct Node));
    node->data = data;

    struct Node *curr = head; 
    struct Node *prev = NULL;

if(head==curr)
{
    addToStart(data);
    return;
}

    while (curr != NULL)
    {

        if (curr->data == insertBefore)
        {
            node->next=prev->next;
            prev->next=node;
            return;
        }
        else
        {
            prev = curr;
            curr=curr->next;
        }
    }
}

void display()
{
    struct Node *curr = head;

    while (curr != NULL)
    {
        printf("%d -> ", curr->data);
        curr = curr->next;
    }

    printf("\n");
}

int main()
{

    printf("Enter at end 10 and 11 \n");
    addEnd(10);
    addEnd(11);

    display();

    printf("\nEnter at start 9 \n");
    addToStart(9);
    display();

    printf("\nEnter at end 12 and 13\n");
    addEnd(12);
    addEnd(13);
    display();

    printf("\nEnter at start 8 and 7 \n");
    addToStart(8);
    addToStart(7);
    display();

    printf("\nEnter 50 after 11 \n");
    addAfter(50, 11);
    display();


  printf("\nEnter 40 before 50 \n");
    addBefore(40,50);
    display();

      printf("\nEnter 1 before heading i.e 40\n");
    addBefore(1,40);
    display();

    return 0;
}