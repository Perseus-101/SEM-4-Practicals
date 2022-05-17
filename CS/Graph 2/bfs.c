#include<stdio.h>
#define MAXSIZE 30

int graph[MAXSIZE][MAXSIZE];
typedef struct queue
{
	int data[MAXSIZE];
	int front,rear;
}QUEUE;

int isempty(QUEUE *pq)
{
	return(pq->front==pq->rear);
}

void addq(QUEUE *pq,int num)
{
	pq->data[++pq->rear]=num;
}

int removeq(QUEUE *pq)
{
	int num;
	++pq->front;
	num=pq->data[pq->front];
	return num;
}

void BFS(int v, int n)
{
	int visited[MAXSIZE];
	QUEUE q;
	q.front=q.rear=-1;
	
    for(int i=0; i<n; i++)
		visited[i]=0;
	
    for(int i=0;i<n;i++)
	{
		addq(&q,v);
		printf("\nVisit\t%d",v);
		visited[v]=1;

		while(!isempty(&q))
		{
			v=removeq(&q);
			for(i=0;i<n;i++)
			{
				if(visited[i]==0 && graph[v][i]!=0)
				{
					addq(&q,i);
					visited[i]=1;
					printf("\nVisit\t%d",i);
				}
			}
		}
	}
}

int main()
{
	int n,v;
	char opt;
	
	printf("\nEnter the number of vertices: ");
	scanf("%d",&n);

	for(int i=0; i<n; i++)
		{
			for(int j=0; j<n; j++)
			{
				printf("Is there an edge between %d and %d?(y/n): ", i, j);
                scanf(" %c", &opt);

                if(opt=='y' || opt=='Y')
                {
                    graph[i][j]=1;
                }
                else
                {
                    graph[i][j]=0;
                }
			}
		}

	printf("\nEnter the starting vertex of BFS: ");
	scanf("%d",&v);

	BFS(v,n);
}