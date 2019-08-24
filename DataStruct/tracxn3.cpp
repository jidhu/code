#include<stdio.h>
#include<iostream>
#include<string.h>

using namespace std;

int main()
{
    char str[] = "jidrhienrdhiria";
    int H[26]={0};
    int length = strlen(str);
    for(int i=0;i<length;i++)
    {
        H[((int)str[i])-97]+=1;
    }
    for(int i=length;i>0;i--)
    {
        if(H[(int)str[i]-97]>=3){cout<<str[i]<<endl;i=0;}
    }
}