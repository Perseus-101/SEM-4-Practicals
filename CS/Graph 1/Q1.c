#include <stdio.h>

int display_matrix(int adj_matrix[][50], int n)
{
    for(int i=0; i<n; i++)
    {
        printf("\n");
        for(int j=0; j<n; j++)
        {
            printf("%d\t", adj_matrix[i][j]);
        }
    }
    return 0;
}

int outdegree(int adj_matrix[][50], int n)
{
    for(int i=0; i<n; i++)
    {
        int out_degree = 0;
        for(int j=0; j<n; j++)
        {
            if(adj_matrix[i][j]==1)
                out_degree++;
        }
        printf("\nOut-degree of vertex %d is: %d", i+1, out_degree);
    }
    return 0;
}

int indegree(int adj_matrix[][50], int n)
{
    for(int j=0; j<n; j++)
    {
        int in_degree = 0;
        for(int i=0; i<n; i++)
        {
            if(adj_matrix[i][j]==1)
                in_degree++;
        }
        printf("\nIn-degree of vertex %d is: %d", j+1, in_degree);
    }
    return 0;
}

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

    outdegree(a,n);
    indegree(a,n);
    display_matrix(a,n);

    return 0;
}