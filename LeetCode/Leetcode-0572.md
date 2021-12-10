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
    bool isSubtree(TreeNode* s, TreeNode* t) {
        if(!s)  return false;
        return judge(s,t)||isSubtree(s->left,t)||isSubtree(s->right,t);
    }
    bool judge(TreeNode *root1,TreeNode *root2){
        if(!root1&&!root2)  return true;
        if(!root1||!root2||root1->val!=root2->val)
            return false;
        return judge(root1->left,root2->left)&&judge(root1->right,root2->right);
    }
};
```