#include <stdio.h>
void swap(int *a, int *b);
int main()
{
    int x=4,y=5;
    printf("%i %i",x,y);
    swap(&x,&y);
    printf("\n%i %i\n",x,y);
    return 0;
}
void swap(int *a, int
{
    *a=*a+*b;
    *b=*a-*b;
    *a=*a-*b;
}
