#include<bits/stdc++.h>
//#include<iostream>
//#include<algorithm>

using namespace std;

int main(void)
{
  string s;
  int count=0;
  cin>>s;
  char vowels[]={'a','e','i','o','u'};

  for (int i=0;i<s.length();i++)
  {
    if ((!binary_search(vowels,vowels+5,s[i]))&&(binary_search(vowels,vowels+5,s[i+1])))
    {
      count++;
      i++;
    }
  }
  cout<<count<<endl;
}
