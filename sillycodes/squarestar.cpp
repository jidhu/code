#include<iostream>
using namespace std;

int main()
{
    int i,j,k,n=5;
    for(i=-n;i<n;i++)
    {
        k=i;
        for(j=0;j<n;j++)
        {
            if(k<=j)
            {
                cout<<"*";
                if(j+1!=n)
                {
                    cout<<" ";
                }
            }
            else
            {
                cout<<" ";
            }
        }
        cout<<"\n";
    }
}
