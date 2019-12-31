#include<iostream>

using namespace std;

int main()
{
    int i,j,k,n=5;
    for (i=-n;i<=n;i++)
    {
        k=i;
        if (i<0)
        {
            k = k* -1;
        }
        for (j=0;j<=n;j++)
        {
            if(j<k)
            {
                cout<<"  ";
            }
            else
            {
                cout<<"*";
            }
        }
        cout<<"\n";
    }
}
