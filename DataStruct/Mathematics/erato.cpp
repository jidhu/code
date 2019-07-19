#include<stdio.h>
#include<iostream>
using namespace std;

void erato(int x)
{
    bool arr[x+1];
    memset(arr[0],true,sizeof(arr));
    
    for(int i=0;i<=x;i++)
    {
        if(arr[i])
        {
            for(int j=i*i;j<=x;j+=i)
            {
                arr[j]=false;
            }
        }
    }
    
    for(int i=0;i<=x;i++)
    {
        if(arr[i])
        {
            cout<<i<<' ';
        }
    }

    cout<<endl;
}

int main()
{
    int n;
    cout<<"Till which number you want to generate prime number?\n> ";
    cin>>n;
    erato(n);
    return 0;
}