#include<iostream>
using namespace std;

int main()
{
    int i,j,k,n=5;
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=n;j++)
        {
            if(i==1||i==n||j==1||j==n)
            {
                cout<<"*";
            }
            else
            {
                cout<<" ";
            }
            if(j!=n)
            {
                cout<<" ";
            }
        }
        cout<<"\n";
    }
}
