#include<iostream>

using namespace std;

struct Node
{
    int data;
    Node *next;
};
void set_data(Node* G,int x)
{
    G -> data = x;
}
int get_data(Node* G)
{
    return G -> data;
}
void set_next(Node* G, Node* GS)
{
    G -> next = GS;
}
void get_next(Node* G)
{
    cout<<G->next;
}
bool has_next(Node *G)
{
    if(G->next != NULL)
    {
        return true;
    }
    return false;
}

int main()
{
    Node *ll = new Node();
    Node *ll2 = new Node();
    set_data(ll,5);
    cout<<get_data(ll);
    set_next(ll,ll2);
    set_data(ll2,7);
    get_next(ll2);

    cout<<has_next(ll);
    cout<<has_next(ll2);
}