#include<stdio.h>

int main()
{
    int arr[] = {1,2,3,4,5,6,7}, d = 2, n = sizeof(arr)/sizeof(int);
    int temp[d], j=0;
    for(int i = 0; i < d; i++)
    {
       temp[i]=arr[i];
    }

    printf("temp[] = [");
    for(int i = 0; i < d; i++){printf("%d ",temp[i]);}
    printf("]\n");

    for(int i = d; i < n; i++)
    {
        arr[j]=arr[i];
        j++;
    }

    printf("arr[] = [");
    for(int i = 0; i < n; i++){printf("%d ",arr[i]);}
    printf("]\n");


    int x=sizeof(temp)/sizeof(int);
    for(int i=0;i<x;i++)
    {
        arr[j]=temp[i];
        j++;
    }

    printf("arr[] = [");
    for(int i = 0; i < n; i++){printf("%d ",arr[i]);}
    printf("]\n");

return 0;
}
