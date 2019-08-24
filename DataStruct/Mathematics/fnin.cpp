#include<stdio.h>
#include<math.h>
#include<iostream>
using namespace std;

void soln1()
{
  long long int x,count=0;
  cout<<"Enter the number?\n> ";
  cin>>x;
  while(x!=0)
  {
    count++;
    x/=10;
  }
  cout<<count<<endl;
}

void soln2()
{
  long long int x,c;
  cout<<"Enter the number?\n> ";
  cin>>x;
  c = log10(x)+1;
  cout<<c<<endl;
}

int main()
{
  soln1();
  soln2();
}
