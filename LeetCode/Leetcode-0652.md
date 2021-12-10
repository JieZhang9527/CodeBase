1. 二叉树的序列化

> 不同二叉树的序列化结果不相同

```C++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        vector<TreeNode*> ans;
        unordered_map<string,int> mp;
        string str=DFS(root,ans,mp);
        return ans;
    }
    string DFS(TreeNode *root,vector<TreeNode*> &ans,unordered_map<string,int> &mp){
        if(!root)   return "#";
        string str=to_string(root->val)+","+DFS(root->left,ans,mp)+","+DFS(root->right,ans,mp);
        if(mp.find(str)!=mp.end()&&mp[str]==1)
            ans.push_back(root);
        mp[str]++;
        return str;
    }
};
```