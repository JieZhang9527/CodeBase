1. 二叉树的序列化

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
    string tree2str(TreeNode* t) {
        string ans;
        if(!t)  return ans;
        ans+=to_string(t->val);
        if(t->left&&t->right)
            ans+="("+tree2str(t->left)+")("+tree2str(t->right)+")";
        else if(t->left)
            ans+="("+tree2str(t->left)+")";
        else if(t->right)
            ans+="()("+tree2str(t->right)+")";
        return ans;
    }
};
```