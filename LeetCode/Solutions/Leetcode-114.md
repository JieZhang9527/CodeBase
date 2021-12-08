1. 递归
> 我们每次需要更改的是右子树，而直接使用先序遍历修改右子树后会导致断链  
> 解决方案：修改遍历顺序为右左根。这样在修改节点右子树时，右子树已遍历完

```C++
class Solution {
public:
    void flatten(TreeNode* root) {
        rightLeftRootOrder(root);
    }
    private:
    TreeNode *pre=nullptr;
    void rightLeftRootOrder(TreeNode *root){
        if(!root)   return;
        rightLeftRootOrder(root->right);
        rightLeftRootOrder(root->left);
        root->left=nullptr;
        root->right=pre;
        pre=root;
    }
};
```