#include<iostream>
using namespace std;

int main()
{
    int i,j,k,n=5;
    for (i=-n;i<=n;i++)
    {
        k=i;
        if(k>0)
        {
            k= k *-1;
        }
        for (j=0;j<n;++j)
        {
            if (j<k+n)
            {
                cout<<" ";
            }
            else
            {
                cout<<"*";
                if(j!=n-1)
                {
                    cout<<" ";
                }
            }
        }
        cout<<"\n";
    }
}
