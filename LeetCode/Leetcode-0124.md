1. 递归
> 遍历每个节点，左子树路径和右子树路径合在一起就是当前节点路径，注意：
> - 为保证子树路径存在的必要性，子树路径和应为max(0,路径和)
> - 求路径和时左右子树都要选，但是求路径最大值时只选一个子树

```C++
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        if(!root)   return 0;
        int ans=root->val;
        help(root,ans);
        return ans;
    }
private:
    int help(TreeNode *root,int &ans){
        if(!root)   return 0;
        int left=max(0,help(root->left,ans));
        int right=max(0,help(root->right,ans));
        ans=max(ans,left+right+root->val);
        return max(left,right)+root->val;
    }
};
```