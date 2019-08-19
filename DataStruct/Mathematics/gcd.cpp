#include<iostream>
#include<algorithm>

using namespace std;
/*
int gcd(int a, int b) { 
   if (a == 0 || b == 0) 
      return 0; 
   else if (a == b) 
      return a; 
   else if (a > b) 
      return gcd(a - b, b); 
   else return gcd(a, b - a);   
} 

int main()
{ 
    int a=12,b=3;
    cout<<gcd(a,b)<<endl;
    return 0;
}*/
int main()
{
    int a = 12, b = 3;
    cout << "gcd(3, 12) = " << __gcd(b, a) << endl; 
}