#include<stdio.h>
#include<algorithm>
#include<iostream>

using namespace std;

int main()
{
    int arr[] = {10, 15, 20, 25, 30, 35}; 
    int n = sizeof(arr)/sizeof(arr[0]);
    
    // using binary_search to check if 20 exists 
    if (binary_search(arr, arr + n, 20)) 
        cout << "20 exists in Array"<<endl; 
    else
        cout << "20 does not exist"<<endl; 
        
    n = upper_bound(arr, arr + n, 16)-arr;
    cout<<n<<endl;
    return 0;
}