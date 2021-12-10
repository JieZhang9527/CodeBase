1. 中序遍历

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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if(!root)   return ans;
        queue<TreeNode*> q;
        q.push(root);
        int depth=0;
        while(!q.empty()){
            int count=q.size();
            vector<int> nums;
            for(int i=0;i<count;++i){
                auto temp=q.front();
                q.pop();
                if(depth%2==0) nums.push_back(temp->val);
                else    nums.insert(nums.begin(),temp->val);
                if(temp->left)  q.push(temp->left);
                if(temp->right) q.push(temp->right);
            }
            ++depth;
            ans.push_back(nums);
        }
        return ans;
    }
};
```

2. DFS

```C++
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        DFS(root,0,ans);
        return ans;
    }
private:
    void DFS(TreeNode *root, int depth, vector<vector<int>> &ans){
        if(!root)   return;
        if(ans.size()==depth)   ans.push_back(vector<int>());
        if(depth%2==0)  ans[depth].push_back(root->val);
        else    ans[depth].insert(ans[depth].begin(),root->val);
        DFS(root->left,depth+1,ans);
        DFS(root->right,depth+1,ans);
    }
};
```