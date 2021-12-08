1. 二叉树层序遍历
> 本质上是BFS，因此需要用队列
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if(!root)   return ans;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            // 记录当前队列元素个数，避免被入队改变
            int count=q.size();
            vector<int> line;
            for(int i=0;i<count;++i){
                auto temp=q.front();
                q.pop();
                line.push_back(temp->val);
                if(temp->left)  q.push(temp->left);
                if(temp->right) q.push(temp->right);
            }
            ans.push_back(line);
        }
        return ans;
    }
};
```
2. DFS

```C++
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if(!root)   return ans;
        DFS(root,0,ans);
        return ans;
    }
private:
    void DFS(TreeNode *root, int depth, vector<vector<int>> &ans){
        if(!root)   return;
        if(ans.size()==depth)   ans.push_back(vector<int>());
        ans[depth].push_back(root->val);
        DFS(root->left,depth+1,ans);
        DFS(root->right,depth+1,ans);
    }
};
```