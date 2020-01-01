#include<iostream>
using namespace std;
int main()
{
    int i,j,k,n=50;
    for(i=-n;i>0;i--)
    {
        k=i; if(k<0){k*=-1;}
        for(j=(k-i)+1;j<=k;j++)
        {
            cout<<j<<" ";
        }
        cout<<"\n";
    }
}
