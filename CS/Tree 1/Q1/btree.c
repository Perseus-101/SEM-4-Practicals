#include<stdio.h>
#include<stdlib.h>
#include"btree.h"

int menu()
{
    int ch;
    printf("\n\n0.Exit\n1.Create BST\n2.Insert Node\n3.Search\n4.inOrder\n5.postOrder\n6.preOrder\nEnter Choice: ");
    scanf("%d", &ch);
    return ch;
}

int main()
{
    struct node*root=NULL;
    int ch;
    while((ch=menu())!=0)
    {
        if(ch==1)
        {
            init(&root);
        }
        else if(ch==2)
        {
            int node;
            printf("\nEnter data: ");
            scanf("%d", &node);
            insert(&root,node);
        }
        else if(ch==3)
        {
            int node;
            printf("\nEnter node to search: ");
            scanf("%d", &node);
            search(root,node);
        }
        else if(ch==4)
        {
            printf("inOrder: ");
            inOrder(root);
        }
        else if(ch==5)
        {
            printf("postOrder: ");
            postOrder(root);
        }
        else if(ch==6)
        {
            printf("preOrder: ");
            preOrder(root);
        }
    }
}