#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};

struct Node *head = NULL;
struct Node *tail = NULL;

void addAtStart(int data)
{
    struct Node *node = malloc(sizeof(struct Node));
    node->data = data;

    if (head == NULL)
    {
        head = node;
        tail = node;
        tail->next = head;
    }
    else
    {
        node->next = head;
        head = node;
        tail->next = head;
    }
}

void addAtEnd(int data)
{
    struct Node *node = malloc(sizeof(struct Node));
    node->data = data;

    if (head == NULL)
    {
        head = node;
        tail = node;
        tail->next = head;
    }
    else
    {
        tail->next = node;
        tail = node;
        tail->next = head;
    }
}

void addAfter(int data, int n)
{

    if (head == NULL)
    {
        printf("List is empty.");
        return;
    }

    struct Node *node = malloc(sizeof(struct Node));
    node->data = data;

    struct Node *curr = head;

    while (curr != NULL)
    {
        if (curr->data == n)
        {
            if (curr == tail)
            {
                addAtEnd(data);
                return;
            }
            node->next = curr->next;
            curr->next = node;
            break;
        }
        else
        {
            curr = curr->next;
        }
    }
    if (curr == NULL)
        printf("Data not found.");
}

void printList()
{
    if (head == NULL)
    {
        printf("List is empty.");
        return;
    }

    struct Node *curr = head;
    do
    {
        printf("%d->", curr->data);
        curr = curr->next;
    } while (curr != head);
    printf("NULL");
    printf("\n");
}

int main()
{

    addAtStart(5);
    addAtStart(3);
    addAtStart(1);
    addAtEnd(14);
    addAtEnd(24);
    printList();
    return 0;
}
