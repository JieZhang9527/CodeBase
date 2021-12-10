1. 递归
> 先建立hash数组可以避免遍历查找

```C++
class Solution {
public:
    TreeNode *buildTree(vector<int>& inorder, vector<int>& postorder) {
        hash(inorder,mp);
        return help(inorder,postorder,0,inorder.size()-1,0,postorder.size()-1);
    }
private:
    unordered_map<int,int> mp;
    void hash(vector<int> &inorder, unordered_map<int,int> &mp){
        for(int i=0;i<inorder.size();++i)  mp[inorder[i]]=i;
    }
    TreeNode *help(vector<int> &inorder,vector<int> &postorder,int inL,int inR,int postL,int postR){
        TreeNode *root=NULL;
        if(postL<=postR)    root=new TreeNode(postorder[postR]);
        else    return root;
        int index=mp[root->val];
        root->left=help(inorder,postorder,inL,index-1,postL,postL+(index-inL)-1);
        root->right=help(inorder,postorder,index+1,inR,postL+(index-inL),postR-1);
        return root;
    }
};
```