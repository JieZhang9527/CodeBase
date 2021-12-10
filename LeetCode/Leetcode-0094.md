1. 中序递归

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
    vector<int> inorderTraversal(TreeNode* root){
        vector<int> ans;
        inOrder(root,ans);
        return ans;
    }
    void inOrder(TreeNode *root, vector<int> &ans){
        if(!root)   return;
        inOrder(root->left,ans);
        ans.push_back(root->val);
        inOrder(root->right,ans);
    }
};
```

2. 中序非递归
> 注意相较于先序非递归，节点值的访问位置

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
    vector<int> inorderTraversal(TreeNode* root){
        vector<int> ans;
        inOrder(root,ans);
        return ans;
    }
    void inOrder(TreeNode *root, vector<int> &ans){
        if(!root)   return;
        stack<TreeNode*> st;
        while(!st.empty()||root){
            while(root){
                st.push(root);
                root=root->left;
            }
            if(!st.empty()){
                ans.push_back(st.top()->val);
                root=st.top()->right;
                st.pop();
            }
        }
    }
};
```