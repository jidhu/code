#include<iostream>
using namespace std;
int main()
{
    int i,j,k,z,n=7;
    for(i=-n;i<n;i++)
    {
        z=i;
        if(z<0)
        {
            z*=-1;
        }
        for(j=1,k=z;j<=z-i;j++,k--)
        {
            if(k<0){
                cout<<k;
            }
            if(j!=z-i){
                cout<<' ';
            }
        }
        cout<<"\n";
    }
}
