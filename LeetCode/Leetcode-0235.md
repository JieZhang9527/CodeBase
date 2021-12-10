1. 二叉树的最近公共祖先（递归）

> 没有利用到二叉搜索树的性质

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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(!root||p==root||q==root)    return root;
        TreeNode *left=lowestCommonAncestor(root->left,p,q);
        TreeNode *right=lowestCommonAncestor(root->right,p,q);
        if(!left)    return right;
        if(!right)   return left;
        return root;
    }
};
```

2. 非递归

```C++
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        while(root){
            if(p->val<root->val&&q->val<root->val)  root=root->left;
            else if(p->val>root->val&&q->val>root->val) root=root->right;
            else    return root;
        }
        return NULL;
    }
};
```