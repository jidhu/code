#include<iostream>
using namespace std;

int main()
{
    int i,j,n=15;
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=(n-i);j++)
        {
            cout<<" ";
        }
        for(j=1;j<=i;j++)
        {
            cout<<"*";
            if(j != (i+1))
            {
                cout<<" ";
            }
        }
        cout<<"\n";
    }
}
