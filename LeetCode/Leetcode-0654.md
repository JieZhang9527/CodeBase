1. 递归

> 如果当前根节点为空，用当前值创建新结点作为根节点  
> 如果当前值大于当前根节点值，当前值创建的结点作为新的根结点，原来的树作为左子树  
> 如果当前值小于当前根结点，将当前值以同样的方式插入右子树  

```C++
class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums){
        TreeNode *root=nullptr;
        for(auto value : nums)
            helper(root,value);
        return root;
    }
    void helper(TreeNode *&root,int value){
        if(!root)   root=new TreeNode(value);
        else if(root->val<value){
            TreeNode *temp=new TreeNode(value);
            temp->left=root;
            root=temp;
        }
        else    helper(root->right,value);
    }
};
```