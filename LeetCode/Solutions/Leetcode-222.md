1. 递归

> 如果某个结点的左子树和右子树一样高，那么左子树是满二叉树；如果某个结点左子树和右子树不一样高，那么右子树是满二叉树

> 计算2^n 使用移位运算 ``1<<n``

```C++
class Solution {
public:
    int countNodes(TreeNode* root) {
        if(!root)   return 0;
        int left=getDepth(root->left);
        int right=getDepth(root->right);
        if(left==right)
            return (1<<left)+countNodes(root->right);
        else
            return (1<<right)+countNodes(root->left);
    }
    int getDepth(TreeNode *root){
        int depth=0;
        while(root){
            ++depth;
            root=root->left;
        }
        return depth;
    }
};
```