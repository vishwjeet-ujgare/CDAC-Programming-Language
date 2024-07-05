#include <stdio.h>
#include <stdlib.h>

// Global head  and  tail
struct Node *head = NULL;
struct Node *tail = NULL;

// struct for node
struct Node
{
    struct Node *prev;
    int data;
    struct Node *next;
};

// It will create a node add data and return it .
struct Node *creatANode(int data)
{
    struct Node *node = malloc(sizeof(struct Node));
    node->next = NULL;
    node->data = data;
    node->prev = NULL;

    return node;
}

// function to add node before head
void insertNodeBeforeHead(int data)
{
    struct Node *node = creatANode(data);

    if (head == NULL)
    {
        // If the linked list is empty , then
        head = node;
        tail = node;
    }
    else
    {
        node->next = head;
        head->prev = node;
        head = node;
    }
}

void insertNodeAtLast(int data)
{
    struct Node *node = creatANode(data);

    if (tail == NULL)
    {
        head = node;
        tail = node;
    }
    else
    {
        tail->next = node;
        node->prev = tail;
        tail = node;
    }
}

void printList()
{
    // storing head pointer in temp
    struct Node *temp = head;

    while (temp != NULL)
    {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
}

void deleteNode(int data)
{
    if (head == NULL && tail == NULL)
    {

        printf("\nLinked List is Emptry..!\n");
        return;
    }
    else if (head->next == NULL && head->data == data)
    {
        // if list having only one head match data if match then dlt it.
        head = NULL;
        tail = NULL;
        printf("\nList Become empty now!\n");
        return;
    }
    else if (head->data == data)
    {
        // If the data to be deleted is at the beginning of linked list
        head->next->prev = NULL;
        head = head->next;
        return;
    }
    else
    {
        struct Node *curr = head;
        struct Node *prev = NULL;

        while (curr != NULL)
        {
            // checking for tail if match then delete node
            if (curr == tail && curr->data == data)
            {
                // deleting the last element of linked
                prev->next = NULL;
                tail = prev;
                return;
            }

            if (curr->data == data)
            {
                prev->next = curr->next;
                curr->next->prev = prev;
                return;
            }
            else
            {
                prev = curr;
                curr = curr->next;
            }
        }
    }
}

int main()
{
    // Create a new Doubly Linked List i.e adding first element to the list
    printf("\nAdding node to first\n");
    insertNodeBeforeHead(50);
    printList();
    printf("\n");

    printf("\nAdding node to first\n");
    insertNodeBeforeHead(40);
    printList();
    printf("\n");

    printf("\nAdding node at last \n");
    insertNodeAtLast(60);
    printList();
    printf("\n");

    printf("\nAdding node at last \n");
    insertNodeAtLast(70);
    printList();
    printf("\n");

    printf("\nDelting 60  \n");
    deleteNode(60);
    printList();
    printf("\n");

    printf("\nDelting 40  \n");
    deleteNode(40);
    printList();
    printf("\n");

    printf("\nDelting 50  \n");
    deleteNode(50);
    printList();
    printf("\n");

    printf("\nDelting 70  \n");
    deleteNode(70);

    printList();


    printf("\n");
}
