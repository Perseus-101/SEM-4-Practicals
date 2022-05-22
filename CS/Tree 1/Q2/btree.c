#include<stdio.h>
#include<stdlib.h>
#include"btree.h"

int menu()
{
    int ch;
    printf("\n\n0.Exit\n1.Create BST\n2.Insert Node\n3.Search\n4.inOrder\n5.postOrder\n6.preOrder\n7.Create\n8.Count Leaf Node\n9.Count non Leaf node\nEnter Choice: ");
    scanf("%d", &ch);
    return ch;
}

int main()
{
    struct node *root=NULL;
    int ch,cnt=0;
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
            printf("\ninOrder: ");
            inOrder(root);
        }
        else if(ch==5)
        {
            printf("\npostOrder: ");
            postOrder(root);
        }
        else if(ch==6)
        {
            printf("\npreOrder: ");
            preOrder(root);
        }
        else if(ch==7)
        {
            int nodes;
            printf("\nHow many nodes to create: ");
            scanf("%d", &nodes);
            create(&root,nodes);
        }
        else if(ch==8)
        {
            cnt=countleaf(root);
            printf("\nNumber of nodes: %d", cnt);
        }
        else if(ch==9)
        {
            cnt=countnonleaf(root);
            printf("\nNumber of nodes: %d", cnt);
        }
    }
}