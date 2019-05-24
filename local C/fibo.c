#include<cs50.h>
#include<stdio.h>

int main()
{

    int n;
    printf("for how many numbers you want in fibonacci series?");
    scanf("%i",&n);
    int i=0,j=1;
    int sum =0;
    while(0<n)
    {
        sum = i+j;
        j=i; i=sum;
        printf("%d\n",sum);
        n--;
    }

}