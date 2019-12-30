#include<iostream>
using namespace std;

int main()
{
    int i,j,k,n=5;
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=(n+1)-i;j++)
        {
            cout<<"*";
        }
        for(k=1;k<i;k++)
        {
            cout<<"  ";
        }
        for(j=1;j<=(n+1)-i;j++)
        {
            cout<<"*";
        }
        cout<<"\n";
    }
    for(i=2;i<=n;i++)
    {
        for(j=1;j<=i;j++)
        {
            cout<<"*";
        }
        for(k=1;k<=n-i;k++)
        {
            cout<<"  ";
        }
        for(j=1;j<=i;j++)
        {
            cout<<"*";
        }
        cout<<"\n";
    }
}
