#include<stdio.h>
#include<cs50.h>

int main(int xxx,string argv[])
{
    if(xxx!=2)
    {
        printf("missing command-line arg");
        return 23;
    }
    printf("%s\n",argv[1]);
}