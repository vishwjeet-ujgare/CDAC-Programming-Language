#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Node
{
    struct Node *prev;
    int data;
    struct Node *next;
};

struct Node *head = NULL;
struct Node *tail = NULL;

bool isListNull()
{

    if (head == NULL && tail == NULL)
    {

        return true;
    }
    else
    {
        return false;
    }
}

struct Node *creatANode(int data)
{
    struct Node *node = malloc(sizeof(struct Node));
    node->data = data;

    // prev and next null
    node->prev = NULL;
    node->next = NULL;
    return node;
}

void displayList()
{
    struct Node *curr = head;

    if (!isListNull())
    {

        while (curr != NULL)
        {
            printf("%d -> ", curr->data);
            curr = curr->next;
        }

        printf(" NULL \n");
    }
    else
    {
        printf("List is empty ...!\n");
    }
    printf("\n");
}

void displayReverseList()
{
    struct Node *curr = tail;

    if (!isListNull())
    {
        while (curr != NULL)
        {
            printf("%d -> ", curr->data);
            curr = curr->prev;
        }

        printf(" NULL \n");
    }
    else
    {
        printf("Tail node does not found .... List is empty \n");
    }
    printf("\n");
}

void addToStart(int data)
{
    struct Node *node = creatANode(data);

    if (isListNull())
    {
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

void addToEnd(int data)
{
    struct Node *node = creatANode(data);

    if (isListNull())
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

void addAfter(int data, int addAfterValue)
{
    struct Node *node = creatANode(data);
    struct Node *curr = head;

    if (isListNull())
    {
        printf("List is empty....\n");
    }
    else if (tail->data == addAfterValue)
    {

        addToEnd(data);
    }
    else
    {

        while (curr != NULL)
        {

            if (curr->data == addAfterValue)
            {
                node->next = curr->next;
                curr->next->prev = node;

                node->prev = curr;
                curr->next = node;
                return;
            }
            else
            {
                curr = curr->next;
            }
        }
    }
}

void delHead()
{

    if (isListNull())
    {
        printf(" List is empty. ");
    }
    else if (head->next == NULL)
    {
        head = NULL;
        tail = NULL;
        printf("list had only one...and...that node has been delted.");
    }
    else
    {
        head = head->next;
        head->prev = NULL;
    }
}

void delTail()
{
    if (isListNull())
    {
        printf(" List is empty. ");
    }
    else if (tail == head)
    {
        head = NULL;
        tail = NULL;
        printf("list had only one node...and...that node has been deleted.\n");
    }
    else
    {
        tail = tail->prev;
        tail->next = NULL;
    }
}

void deleteNode(int data)
{

    struct Node *curr = head;
    if (isListNull())
    {
        printf("Node not found ....Due to List is empty.\n");
    }
    else if (head->data == data)
    {
        head = curr->next;
        head->prev = NULL;
    }
    else if (tail->data == data && tail->next == NULL)
    {

        tail = tail->prev;
        tail->next = NULL;

        return;
    }
    else
    {
        while (curr != NULL)
        {
            if (curr->data == data)
            {
                curr->prev->next = curr->next;
                curr->next->prev = curr->prev;
                return;
            }
            else
            {
                curr = curr->next;
            }
        }
    }
}

void delAfter(int data)
{
    struct Node *curr = head;

    if (isListNull())
    {
        printf("Node not found ....List is empty. \n");
    }
    else if (head->next == NULL)
    {
        printf("Bhai bhai bhai kya delete karna chahta hai bhaii ..list main only %d ekk hi to node hai(i.e head).%d ke agge to null hai bhai.Delete head use karle bhaii..\n", head->data, head->data);
    }
    else if (tail->data == data && tail->next == NULL)
    {
        printf("Bhai bhai ye circular linked list nahi hai ...%d ke aage(tail) null hai bhai..Delete tail use karle bhai\n\n", data);
    }
    else
    {

        while (curr != NULL)
        {

            if (curr->data == data)
            {

                if (curr->next->next == NULL)
                {

                    curr->next->prev = NULL;
                    curr->next = NULL;
                    tail = curr;
                    //   printf("%d \n",curr->next->data);
                    // deleteNode(curr->next->data);

                    return;
                }
                else
                {
                    curr->next = curr->next->next;
                    curr->next->prev = curr;
                    return;
                }
            }
            else
            {
                curr = curr->next;
            }
        }

        printf("Entered Node with data %d  is not found \n", data);
    }
}

void delBefore(int data)
{
    struct Node *curr = head;
    if (isListNull())
    {
        printf("Link is NULL \n");
    }
    else if (head->data == data)
    {
        printf("No no  before head . ca \n");
    }

    else
    {

        while (curr != NULL)
        {

            if (curr->data == data)
            {
                if (curr->prev->prev == NULL)
                {
                    head = curr;
                    head->prev = NULL;
                    return;
                }
                else
                {
                    curr->prev = curr->prev->prev;
                    curr->prev->next = curr;
                    break;
                }
            }
            else
            {
                curr = curr->next;
            }
        }

        printf("Entered Node with data %d  is not found \n", data);
    }
}
int main()
{
    printf("\n");
    printf("Adding data for the first time ..\n");
    addToStart(50);
    displayList();

    printf("Adding data 40 to start ..\n");
    addToStart(40);
    displayList();

    printf("The list in reverse order \n");
    displayReverseList();

    printf("Adding data at the end \n");
    addToEnd(30);
    displayList();

    printf("Adding data at the end \n");
    addToEnd(20);
    displayList();

    printf("Adding 45  after 50  \n");
    addAfter(45, 50);
    displayList();

    printf("Delete 30 node from list  \n");
    deleteNode(40);
    displayList();

    printf("Adding 45  after 50  \n");
    addAfter(55, 50);
    displayList();

    printf("Deleting head \n");
    delHead();
    displayList();

    printf("Deleting tail \n");
    delTail();
    displayList();

    printf("Deleting after 45 \n");
    delAfter(45);
    displayList();

    printf("Deleting before 45 \n");
    delBefore(45);
    displayList();


   
}
