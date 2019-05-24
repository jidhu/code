#include<stdio.h>
#include<cs50.h>

int main()
{
    while(true)
    {
        int a=get_int("Enter the Value");
        if(a%2==0)
        {
            printf("Your value is a even number ");
            break;
        }
    }
}