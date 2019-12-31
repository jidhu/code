#include<iostream>
using namespace std;

int main()
{
    int i,j,k,n=25;
    for(i=1;i<=n;i++)
    {
        for(j=1;j<i;j++)
        {
            cout<<" ";
        }
        for(j=0;j<=n-i;j++)
        {
            if(j==n-i||j==0||i==1){cout<<"*";}
            else{cout<<" ";}
        }
        cout<<"\n";
    }
}
