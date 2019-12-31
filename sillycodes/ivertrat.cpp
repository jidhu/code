#include<iostream>
using namespace std;

int main()
{
    int i,j,k,n=25;
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=(n-i)+1;j++)
        {
            if(i==1||j==1||i+j==n+1){cout<<"*";}
            else{cout<<" ";}
        }
        cout<<"\n";
    }
}
