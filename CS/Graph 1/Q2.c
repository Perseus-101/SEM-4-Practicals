#include <stdio.h>
#include <stdlib.h>

#define newnode (struct node*)malloc(sizeof(struct node))

struct node{
    int vertex;
    struct node *next;
};

int outdegree(struct node *adj_list[], int n)
{
    struct node *temp;
    for(int i=0; i<n; i++)
    {
        temp=adj_list[i];
        int out_degree=0;
        while(temp!=NULL)
        {
            out_degree++;
            temp=temp->next;
        }
        printf("\nOut-degree of vertex is %d is: %d", i+1, out_degree);
    }
}
int main()
{
    int n;
    char opt;
    struct node *a[50], *p, *c;

    printf("\nEnter number of vertices: ");
    scanf("%d", &n);

    for(int i=0; i<n; i++)
        a[i]=NULL;

    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
            printf("Is there an edge between %d and %d?(y/n): ", i+1, j+1);
            scanf(" %c", &opt);

            if(opt=='y' || opt=='Y')
            {
                c=newnode;
                c->vertex=j;
                c->next=NULL;

                if(a[i]==NULL)
                    a[i]=c;
                else
                {
                    p=a[i];
                    while(p->next!=NULL)
                        p=p->next;
                    p->next=c;
                }
            }
        }
    }

    outdegree(a,n);
}