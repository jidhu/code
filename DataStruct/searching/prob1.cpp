#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int T;
	cin>>T;
	while(T>0)
	{
	    int n,x;
	    cin>>n;
	    int arr[n];
	    for(int i=0; i<n; i++)
        {
            cin>>arr[i];
        }
        cin>>x;
        if (binary_search(arr,arr+n,x))
        {
            return binary_search(arr,arr+n,x);
        }
        return -1;
    }
}