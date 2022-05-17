#include<stdio.h>
#define MAX 20

int graph[10][10];
typedef struct 
{
	int items[MAX];
	int top;
}stack;

void init(stack *ps)
{
	ps->top=-1;
}

void push(stack *ps,int n)
{
	ps->top++;
	ps->items[ps->top]=n;
}

int pop(stack *ps)
{
	return(ps->items[ps->top--]);
}

int isempty(stack *ps)
{
	return ps->top==-1;
}

int isfull(stack *ps)
{
	return(ps->top==MAX-1);
}

void DFS(int v, int n)
{
	int found;
	int visited[20]={0};
	stack s;	
	init(&s);
	visited[v]=1;
	push(&s,v);
	printf("\nVisit %d",v);
	while(1)
	{
		found=0;
		for(int i=0; i<n; i++)
		{
			if((graph[v][i]==1)&&(visited[i]==0))
			{
				push(&s,i);
				printf("\nVisit %d", i);
				visited[i]=1;
				v=i;
				found=1;
				break;
			}
		}
		if(found==0)
		{
			if(isempty(&s))
				break;
			else
				v=pop(&s);
		}
	}
}

int main()
{
	int v,n;
	char opt;
	printf("\nEnter the number of vertices: ");
	scanf("%d",&n);

	for(int i=0; i<n; i++)
		{
			for(int j=0; j<n; j++)
			{
				printf("\nIs there edge between %d and %d?(y/n)",i,j);
				scanf(" %c",&opt);
				if(opt=='y')
					graph[i][j]=1;
				else
					graph[i][j]=0;
			}
		}
	printf("\nEnter the starting vertex of DFS: ");
	scanf("%d",&v);

	DFS(v,n);

    return 0;
}