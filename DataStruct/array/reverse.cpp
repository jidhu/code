#include<stdio.h>
#include<iostream>
#include<string.h>

using namespace std;

int reverseArray(int arr[],int start,int end,int n) 
{ 
    if (start >= end) 
        return 0; 
    int temp;
    // Swap elements at start and end  
    temp = arr[start];  
    arr[start] = arr[end];
    arr[end] = temp; 
    
    // Recursive Function calling 
    reverseArray(arr, start + 1, end - 1,n);
    
}

int main()
{
    int arr[]={1,2,3,4,5,6,7,8,9};
    int n =sizeof(arr)/sizeof(int);
    for(int i=0;i<n;i++){cout<<arr[i];}cout<<endl;

    int start=0,end=n-1;

    reverseArray(arr,start,end,n);
    
    for(int i=0;i<n;i++){cout<<arr[i];}cout<<endl;
   
    return 0;
}