#include<iostream>
using namespace std;

int main()
{
	int i,j,n=5;
	
	for(i=1; i<=n; i++)
	{
		for(j=1; j<=n; j++)
		{
			if ((i==j) || (n==(i+j)-1))
			{
				cout<<"*";
			}
			else
			{
				cout<<" ";
			}
		}
		cout<<"\n";
	}
}
