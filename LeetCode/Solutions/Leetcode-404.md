1. 递归

```C++
class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        if(!root)   return 0;
        int left=sumOfLeftLeaves(root->left);
        int right=sumOfLeftLeaves(root->right);
        int sum=left+right;
        if(root->left&&!root->left->left&&!root->left->right)
            sum+=root->left->val;
        return sum;
    }
};
```