1. 递归
> 自顶向下会产生大量重复计算
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
    bool isBalanced(TreeNode* root) {
        if(!root)   return true;
        int left=height(root->left);
        int right=height(root->right);
        if(abs(left-right)>1)   return false;
        return isBalanced(root->left)&&isBalanced(root->right);
    }
    int height(TreeNode *root){
        if(!root)   return 0;
        return max(height(root->left),height(root->right))+1;
    }
};
``` 

1. 递归
> 自底向上，提前阻断
```C++
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        return heightOfTree(root)!=-1;
    }
    int heightOfTree(TreeNode *root){
        if(!root)   return 0;
        int left=heightOfTree(root->left);
        if(left==-1)    return -1;
        int right=heightOfTree(root->right);
        if(right==-1)   return -1;
        if(abs(left-right)<2)   return max(left,right)+1;
        return -1;
    }
};
```