'''T = int(input())
while(T>0):
    size = int(input())
    arr = list(map(int,input().split()))
    res = []
    for i in range(size):
        if i+1 == len(arr):
            break
        res.append(arr[i] & arr[i+1])
    if len(res) == 0:
        print(0)
    else:
        print(max(res))
    T-=1'''

'''#include<bits/stdc++.h>
using namespace std;

// Utility function to check number of elements
// having set msb as of pattern
int checkBit(int pattern, int arr[], int n)
{
    int count = 0;
    for (int i = 0; i < n; i++)
        if ((pattern & arr[i]) == pattern)
            count++;
    return count;
}

// Function for finding maximum and value pair
int maxAND (int arr[], int n)
{
    int res = 0, count;

    // iterate over total of 30bits from msb to lsb
    for (int bit = 31; bit >= 0; bit--)
    {
        // find the count of element having set  msb
        count = checkBit(res | (1 << bit),arr,n);

        // if count >= 2 set particular bit in result
        if ( count >= 2 )
            res |= (1 << bit);
    }

    return res;
}

// Driver function
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        int arr[n],i;
        for(i=0;i<n;i++)
        cin>>arr[i];
    cout <<  maxAND(arr,n)<<endl;
    }
    return 0;
}'''
def checkBit(pattern,arr,n):
    count = 0
    for i in n:
        if ((pattern & arr[i]) == pattern):
            count+=1
    return count

def maxAND(arr,n):
    res =0
    for bit in range(31,-1):
        count = checkBit(res | (1 << bit),arr,n)
        if( count >= 2 ):
            res |= (1 << bit)
    return res

T = int(input())
while(T>0):
    size = int(input())
    arr = list(map(int,input().split()))
    print(maxAND(arr,size))
    T-=1