#include<stdio.h>
int y;

void displayarr(int a[], int n)
{
    for(int i=0; i<n; i++)
        printf(" %d",a[i]);
}

void heapify(int a[], int n, int i)
{
	int large=i, l=2*i+1, r=2*i+2;

	if(l < n && a[l] > a[large])
		large=l;
	if(r < n && a[r] > a[large])
		large=r;
	if(large!=i)
	{
		int temp = a[i];
		a[i]=a[large];
		a[large]=temp;
		heapify(a,n,large);
	}

    if(y==n)
    {
        printf("\nThe array will be: ");
        displayarr(a,n);
        y--;
    }
}

void heapsort(int a[],int n)
{
	for(int i=n/2-1;i>=0;i--)
		heapify(a,n,i);
	for(int i=n-1;i>=0;i--)
	{
		int temp = a[0];
		a[0] = a[i];
		a[i] = temp;
		heapify(a,i,0);	
	}
}

int main()
{
	int arr[50], n;

	printf("\nHow many numbers to enter: ");
	scanf("%d",&n);
	for(int i=0;i<n;i++)
    {
        printf("\nEnter element [%d]: ",i);
		scanf("%d",&arr[i]);
    }
    y=n;
	
	printf("\nThe elements before sorting are: ");
	for(int i=0;i<n;i++)
		printf(" %d",arr[i]);

	heapsort(arr,n);

	printf("\nThe elements after sorting are: ");
	for(int i=0;i<n;i++)
		printf(" %d",arr[i]);

    return 0;
}



