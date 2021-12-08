1. 递归
> preL和preR分别表示先序序列的左右边界

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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return help(preorder,inorder,0,preorder.size()-1,0,inorder.size()-1);
    }
private:
    TreeNode *help(vector<int> &preorder,vector<int> &inorder,int preL,int preR,int inL,int inR){
        if(preL>preR)   return NULL;
        TreeNode *root=new TreeNode(preorder[preL]);
        int index=inL;
        while(inorder[index]!=root->val)    ++index;
        int len=index-inL;
        root->left=help(preorder,inorder,preL+1,preL+1+len-1,inL,inL+len-1);
        root->right=help(preorder,inorder,preL+len+1,preR,index+1,inR);
        return root;
    }
};
```