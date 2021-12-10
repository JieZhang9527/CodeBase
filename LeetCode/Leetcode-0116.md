1. 层序遍历
> 非常量空间

```C++
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/
class Solution {
public:
    Node* connect(Node* root) {
        levelOrder(root);
        return root;
    }
private:
    void levelOrder(Node *root){
        if(!root)   return;
        queue<Node*> q;
        q.push(root);
        while(!q.empty()){
            int count=q.size();
            Node *pre=NULL;
            for(int i=0;i<count;++i){
                Node *temp=q.front();
                q.pop();
                if(pre) pre->next=temp;
                pre=temp;
                if(temp->left)  q.push(temp->left);
                if(temp->right) q.push(temp->right);
            }
        }
    }
};
```

2. 拉链法
> 自己模拟一下，每次将节点的左右子树链接在一起

```C++
class Solution {
public:
    Node* connect(Node* root) {
        if(!root)   return NULL;
        Node *left=root->left;
        Node *right=root->right;
        while(left){
            left->next=right;
            left=left->right;
            right=right->left;
        }
        connect(root->left);
        connect(root->right);
        return root;
    }
};
```

3. 递归
```C++
class Solution {
public:
    Node* connect(Node* root) {
        if(!root||!root->left)   return root;
        root->left->next=root->right;
        if(root->next)
            root->right->next=root->next->left;
        connect(root->left);
        connect(root->right);
        return root;
    }
};
```