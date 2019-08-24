#include <stdio.h>
#include <iostream>
 
int main()
{
    int row,c,s,space,chr;
    int n=3;
    int s=n;
    int c=1;
    
    for (row=1;row<2*n-1;row++)
    {
        if (s>=0)
        {
            for (space=s-1;space>0;space--)
            {
                cout<<' ';
            }
        
        
            for (chr=1;chr<=c;c++)
            {
                cout<<'*';
                if(chr<c)
                {
                    cout<<' ';
                }
            }
            cout<<endl;
        
            c++;
            s--;
        }
    }