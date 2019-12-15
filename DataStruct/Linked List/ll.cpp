#include<stdio.h>
#include<iostream>
#include<algorithm>

using namespace std;

struct Node{
    int key;
    Node *next;
    Node (int x)
    {
    key = x;
    next = NULL;
    }
};

Node *insertBegin(Node *head, int key)
{
    Node *temp = new Node(key);
    temp -> next = head;
    return temp;
}

void printlist(Node *head)
{
    Node *curr = head;
    while(curr != NULL)
    {
        cout<<(curr->key)<<" ";
        curr = curr -> next;
    }
}

int main()
{
    Node *head = NULL;
    head = insertBegin(head, 20);
    head = insertBegin(head, 5);
    head = insertBegin(head, 10);
    printlist(head);
    return 0;
}
