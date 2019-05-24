#include<stdio.h>
//#include<cs50.h>

int main(int argc,string argv[])
{
    printf("Total strings are %i\n",argc);
    for(int i=0;i<argc;i++)
    {
        printf("%s\n",argv[i]);
    }
}
