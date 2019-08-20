#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int T;
	cin>>T;
	while(T>0)
	{
	    int n,temp,x,i=0;
	    cin>>n;
	    int arr[n];
	    cin>>temp;
	    
	    while(i < n)
    	{	
    	    arr[n] = temp;
	    	i++;
		}
		
	    for(i=0; i<n; i++)
        {
        cin>>arr[i];
        }
        cin>>x;
        
        if (binary_search(arr,arr+n,x))
        {
            cout<<binary_search(arr,arr+n,x);
        }
        cout<<-1;
	}
	T--;
}
