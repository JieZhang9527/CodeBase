1. 递归

> 注意函数的返回值包含选择根节点和不选择根节点  
> 先计算左子树和右子树的结果可以将计算方式改为自底向上

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
    int rob(TreeNode* root) {
        auto ans=DFS(root);
        return max(ans.first,ans.second);
    }
private:
    pair<int,int> DFS(TreeNode* root){
        if(!root)   return make_pair(0,0);
        auto left=DFS(root->left);
        auto right=DFS(root->right);
        int no_select=max(left.first,left.second)+max(right.first,right.second);
        int select=root->val+left.second+right.second;
        return make_pair(select, no_select);
    }
};
```