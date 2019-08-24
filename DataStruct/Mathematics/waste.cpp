#include<stdio.h>
#include<iostream>
#include<string.h>
using namespace std;

void erato(int n)
{
  bool prime[n+1];
  memset(prime,true,sizeof(prime));

  for(int i=2;i*i<=n;i++)
  {
    if (prime[i]==true)
    {
      for (int j=i*i;j<=n;j+=i)
      {
        prime[j]=false;
      }
    }
  }
  int count=0;
  for (int x=2;x<=n;x++)
  {
    if (prime[x]==true)
    {
      cout<<x<<'\t';
      count++;
    }
  }
  cout<<endl<<endl<<"Total prime numbers till "<<n<<" are "<<count<<endl;
}

int main()
{
  int n;
  cout<<"till which prime numbers you generate?\n> ";
  cin>>n;
  erato(n);
  return 0;
}
