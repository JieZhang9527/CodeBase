1. 递归

```C++
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(!root)   return NULL;
        TreeNode *temp=root->left;
        root->left=root->right;
        root->right=temp;
        invertTree(root->left);
        invertTree(root->right);
        return root;
    }
};
```

2. BFS

```C++
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        BFS(root);
        return root;
    }
private:
    void BFS(TreeNode *root){
        if(!root)   return;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            TreeNode *temp=q.front()->left;
            q.front()->left=q.front()->right;
            q.front()->right=temp;
            temp=q.front();
            q.pop();
            if(temp->left)  q.push(temp->left);
            if(temp->right) q.push(temp->right);
        }
    }
};
```

3. DFS

```C++
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        DFS(root);
        return root;
    }
private:
    void DFS(TreeNode *root){
        if(!root)   return;
        TreeNode *temp=root->left;
        root->left=root->right;
        root->right=temp;
        DFS(root->left);
        DFS(root->right);
    }
};
```