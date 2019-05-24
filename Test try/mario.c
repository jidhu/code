#include<stdio.h>

int main()
{
    int n;
    printf("Enter the height: ");
    scanf("%d",&n);
    int i=0 ,k=n-3;
    if (n>0)
        {
         for (i=0;i<n;i++)
         {
             printf(" ");
             for (int j=0;j<k;j++)
                {
                    printf("#");
                }
            k+=1;
            printf("\n");
         }
        }
    return 0;
}