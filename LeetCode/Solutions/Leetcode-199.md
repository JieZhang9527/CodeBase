1. 层次遍历

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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ans;
        if(!root)   return ans;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            int count=q.size();
            for(int i=0;i<count;++i){
                TreeNode *temp=q.front();
                if(i==count-1)  ans.push_back(temp->val);
                q.pop();
                if(temp->left)  q.push(temp->left);
                if(temp->right) q.push(temp->right);
            }
        }
        return ans;
    }
};
```

2. 递归
> 注意每次先遍历右子树
```C++
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ans;
        DFS(root,0,ans);
        return ans;
    }
private:
    void DFS(TreeNode *root, int depth, vector<int> &ans){
        if(!root)   return;
        if(ans.size()==depth)   ans.push_back(root->val);
        DFS(root->right,depth+1,ans);
        DFS(root->left,depth+1,ans);
    }
};
```