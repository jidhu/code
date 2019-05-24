#include<stdio.h>
#include<cs50.h>
int fib(int);
int main()
{
    int n;
    printf("for how many numbers you want in fibonacci series? ");
    scanf("%i",&n);
    fib(n);
}
int fib(x)
{
    if (x==0) {return 0;}
    else if(x==1) {return 1;}
    else {printf("%i\n",fib(x-1) + fib(x-2)); return 0;}
}