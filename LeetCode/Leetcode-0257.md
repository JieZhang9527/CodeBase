1. DFS

> 注意这里的path使用传值调用

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
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> ans;
        string path;
        DFS(root,path,ans);
        return ans;
    }
private:
    void DFS(TreeNode *root, string path, vector<string> &ans){
        if(!root)   return;
        if(!root->left&&!root->right){
            path+=to_string(root->val);
            ans.push_back(path);
        }
        else    path+=to_string(root->val)+"->";
        DFS(root->left,path,ans);
        DFS(root->right,path,ans);
    }
};
```