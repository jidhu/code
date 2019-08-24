#include <stdio.h>
#include <iostream>
using namespace std;

int main()
{
    int row,space,chr;
    int n=3;
    int s=n;
    int c=1;

    for (row=1;row<=n;row++)
    {
        for (space=s-1;space>0;space--)
        {
            cout<<' ';
        }

        for (chr=1;chr<=c;chr++)
        {
            cout<<'*';
            if(chr<c)
            {
                cout<<'#';
            }
        }
        cout<<endl;
        c++;
        s--;
    }
        c--;
        s+=2;

    for (row=n;row<2*n-1;row++)
    {
        for (space=1;space<s;space++)
        {
            cout<<' ';
        }

        for (chr=c-1;chr>0;chr--)
        {
            cout<<'*';
            if(chr>=c-1)
            {
                cout<<'#';
            }
        }
        cout<<endl;
        c--;
        s++;
    }

    return 0;
}
