1. 层序遍历
> 本质是BFS

```C++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int minDepth(TreeNode* root) {
        if(!root)   return 0;
        queue<TreeNode*> q;
        q.push(root);
        int depth=1;
        while(!q.empty()){
            int count=q.size();
            for(int i=0;i<count;++i){
                auto temp=q.front();
                q.pop();
                if(!temp->left&&!temp->right)   return depth;
                if(temp->left)  q.push(temp->left);
                if(temp->right) q.push(temp->right);
            }
            ++depth;
        }
        return depth;
    }
};
```

2. DFS

```C++
class Solution {
public:
    int minDepth(TreeNode* root) {
        if(!root)   return 0;
        int min_depth=INT_MAX;
        DFS(root,1,min_depth);
        return min_depth;
    }
private:
    void DFS(TreeNode *root, int depth, int &min_depth){
        if(!root)   return;
        if(!root->left&&!root->right)   min_depth=min(min_depth,depth);
        DFS(root->left,depth+1,min_depth);
        DFS(root->right,depth+1,min_depth);
    }
};
```