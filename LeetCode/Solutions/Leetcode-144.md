1. 递归

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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        preOrder(root,ans);
        return ans;
    }
private:
    void preOrder(TreeNode *root,vector<int> &ans){
        if(!root)   return;
        ans.push_back(root->val);
        preOrder(root->left,ans);
        preOrder(root->right,ans);
    }
};
```

2. 非递归
> 本质上是DFS，因此需要用到栈

```C++
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        preOrder(root,ans);
        return ans;
    }
private:
    void preOrder(TreeNode *root,vector<int> &ans){
        stack<TreeNode*> st;
        while(root||!st.empty()){
            while(root){
                ans.push_back(root->val);
                st.push(root);
                root=root->left;
            }
            if(!st.empty()){
                root=st.top()->right;
                st.pop();
            }
        }
    }
};
```