#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    //get te string from the user
    string s=get_string("give a word: ");
    // intialize the var a= space, i=forward, j= backward, k=mid space
    int a,i,x,j,k,mid,n=strlen(s); mid=(n/2); j=n-1; k=n-2;
    if(n%2!=0)
    {
    //iterate the char in string
        for(i=0;i<n;i++)
        {
            //iterate the spaces before the string prints
        for(a=0; a<i; a++)
        {
            printf(" ");
        }
        //print the forward string
        printf("%c",s[i]);
        //iterate the space for mid
        for(x=0;x<k;x++)
        {
            printf(" ");
        }
        //print the reverse string
        if(mid==i)
        {
            break;
        }
        printf("%c\n",s[j]);
        //decrement the j for reverse string and k is decrement for spaces
        j-=1; k-=2;
        }
    printf("\n");
    k=0; j=mid+1;
    for(i=mid-1;i>=0;i--)
    {
        //iterate for front space
        for(a=i;a>0;a--)
        {
            printf(" ");
        }
        //print the forward string
        printf("%c",s[i]);
        //iterate the space for mid
        for(x=0;x<=k;x++)
        {
            printf(" ");
        }
        //print the reverse string
        printf("%c\n",s[j]);
        //increment the j for reverse string and k is increment for spaces
        j+=1; k+=2;
    }
    }
    else
    {
        printf("please enter the string again whose characters should be a odd number\n");
    }
}