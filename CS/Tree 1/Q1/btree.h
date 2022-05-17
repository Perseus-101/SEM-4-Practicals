struct node
{
    int data;
    struct node *left, *right;
};

struct node *createnode(struct node *newnode, int data)
{
    newnode = malloc(sizeof(struct node));
    newnode->data = data;
    newnode->left = newnode->right=NULL;
    return newnode;
}

void insert(struct node **root, int data)
{
    struct node *newnode;
    newnode = createnode(newnode, data);
    if(*root==NULL)
        *root = newnode;
    else
    {
        struct node *temp = *root;
        while(1)
        {
            if(data<=temp->data)
            {
                if(temp->left==NULL)
                {
                    temp->left = newnode;
                    break;
                }
                temp = temp->left;
            }
            else
            {
                if(temp->right==NULL)
                {
                    temp->right = newnode;
                    break;
                }
                temp = temp->right;
            }
        }
    }
}

void init(struct node **root)
{
    struct node *temp=(struct node*)malloc(sizeof(struct node));
    temp->left=NULL;
    temp->right=NULL;
}

void inOrder(struct node *temp)
{
    if(temp)
    {
        inOrder(temp->left);
        printf("%d ", temp->data);
        inOrder(temp->right);
    }
}

void preOrder(struct node *temp)
{
    if(temp)
    {
        printf("%d ",temp->data);
        preOrder(temp->left);
        preOrder(temp->right);
    }
}

void postOrder(struct node *temp)
{
    if(temp)
    {
        postOrder(temp->left);
        postOrder(temp->right);
        printf("%d ",temp->data);
    }
}

int search(struct node *temp, int data)
{
    if(temp)
    {
        if(temp->data==data)
        {
            printf("\nData Found!");
            return 0;
        }
        search(temp->left,data);
        search(temp->right,data);
    }
}