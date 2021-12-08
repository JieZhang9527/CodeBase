1. 递归
> 本题的关键思想是自己和自己相比

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
    bool isSymmetric(TreeNode* root) {
        return help(root,root);
    }
private:
    bool help(TreeNode *root1, TreeNode *root2){
        if(!root1&&!root2)  return true;
        if(!root1||!root2||root1->val!=root2->val)  return false;
        return help(root1->left,root2->right)&&help(root1->right,root2->left);
    }
};
```