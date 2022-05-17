#include <stdio.h>

int main()
{
    int n;
    char opt;
    int a[50][50];

    printf("\nEnter number of vertices: ");
    scanf("%d", &n);

    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
            printf("Is there an edge between %d and %d?(y/n): ", i+1, j+1);
            scanf(" %c", &opt);

            if(opt=='y' || opt=='Y')
            {
                a[i][j]=1;
            }
            else
            {
                a[i][j]=0;
            }
        }
    }

    int check=0;
    for (int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
            if(a[i][j]!=a[j][i])
                check=1;
        }
    }

    if(check!=1)
        printf("\nThe Graph is undirected");
    else
        printf("\nThe Graph is directed");

    return 0;
}