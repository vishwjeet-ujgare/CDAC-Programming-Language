#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};

struct Node *head = NULL;
struct Node *tail = NULL;

void addToEnd(int data)
{
    struct Node *node = malloc(sizeof(struct Node));
    node->data = data;

    if (head==NULL)
    {
        head=node;
        tail=node;
        tail->next=head;
    }
    else{
        tail->next=node;
        tail=node;
        tail->next=head;
    }
}



void displayCicularLL()
{
    
}