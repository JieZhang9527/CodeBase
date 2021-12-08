> 任一条路径可以被看作是以某个节点为起点，左子树和右子树的路径拼接而成

1. DFS 
   
```C++
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int ans=0;
        Height(root,ans);
        return ans;
    }
private:
    int Height(TreeNode *root, int &ans){
        if(!root)   return 0;
        int left=Height(root->left,ans);
        int right=Height(root->right,ans);
        ans=max(ans,left+right);
        return max(left,right)+1;
    }
};
```