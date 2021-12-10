1. DFS 

> 先求树的高度，初始化结果矩阵。深度优先遍历，填充相应的值

```C++
class Solution {
public:
    vector<vector<string>> printTree(TreeNode* root) {
        int depth=getDepth(root);
        vector<vector<string>> ans(depth,vector<string>((1<<depth)-1,""));
        DFS(root,1<<(depth-1),0,((1<<depth)-1)>>1,ans);
        return ans;
    }
    int getDepth(TreeNode *root){
        if(!root)   return 0;
        return max(getDepth(root->left),getDepth(root->right))+1;
    }
    void DFS(TreeNode *root,int len,int row,int column,vector<vector<string>> &ans){
        if(!root)   return;
        ans[row][column]=to_string(root->val);
        len>>=1;
        DFS(root->left,len,row+1,column-len,ans);
        DFS(root->right,len,row+1,column+len,ans);
    }
};
```