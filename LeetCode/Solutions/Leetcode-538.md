1. 逆中序遍历

> 二叉搜索树中序遍历 左根右 从小到大遍历，逆中序遍历 右根左 从大到小遍历，从大到小遍历时，保存前一个累加结点的值，与当前结点的值加和。

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
    TreeNode* convertBST(TreeNode* root) {
        stack<TreeNode*> st;
        TreeNode *copy=root;
        int sum=0;
        while(root||!st.empty()){
            while(root){
                st.push(root);
                root=root->right;
            }
            if(!st.empty()){
                auto temp=st.top();
                st.pop();
                temp->val+=sum;
                sum=temp->val;
                root=temp->left;
            }
        }
        return copy;
    }
};
```

2. 递归

```C++
class Solution {
public:
    TreeNode* convertBST(TreeNode* root) {
        if(!root)   return root;
        convertBST(root->right);
        sum+=root->val;
        root->val=sum;
        convertBST(root->left);
        return root;
    }
private:
    int sum=0;
};
```