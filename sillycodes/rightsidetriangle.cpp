#include<iostream>
using namespace std;
int main()
{
   int i,j,k,num=5;
 
   for(i=-num;i<num;i++)
   {
      k=i;
      if(k<0)
      {
         k = k * -1;
      }
      for (j = 0; j < num; ++j)
      {
         if (j<k)
         {
            cout<<"  ";   // two spaces
         }
         else
         {
            cout<<" *";   // one star, one space.
         }
      }
      cout<<"\n";
   }
   return 0;
}
