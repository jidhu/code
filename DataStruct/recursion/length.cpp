#include<bits/stdc++.h>

using namespace std;
int getmax(int len, int a, int b, int c)
{
  if (len<0)
  {
    return -1;
  }
  if (len==0)
  {
    return 0;
  }
  int ca = getmax(len-a,a,b,c);
  int cb = getmax(len-b,a,b,c);
  int cc = getmax(len-c,a,b,c);
  int res=0;
  if ((ca>=cb)&&(ca>=cc)) { res = ca; return ca;}
  else if (b>=c) {res=cb; return cb;}
  else {res = cc;return cc;}
  if (res==-1)
  {
    return -1;
  }
  else
  {
    return res+1;
  }
}

int main()
{
  int len = 5;
  int a=1,b=2,c=3;
  std::cout<<getmax(len,a,b,c);
  return 1;
}
