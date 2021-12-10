1. 递归1
> 根据二叉搜索树的特性，子树也是一棵二叉搜索树

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
    bool isValidBST(TreeNode* root) {
        if(!root)   return true;
        if((!root->left||leftMax(root->left)<root->val)&&(!root->right||rightMin(root->right)>root->val))
            return isValidBST(root->left)&&isValidBST(root->right);
        return false;
    }
private:
    int leftMax(TreeNode *root){
        int ans=-1;
        while(root){
            ans=root->val;
            root=root->right;
        }
        return ans;
    }
    int rightMin(TreeNode *root){
        int ans=-1;
        while(root){
            ans=root->val;
            root=root->left;
        }
        return ans;
    }
};
```

2. 递归
> 维护当前访问节点所在的数值范围

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
    bool isValidBST(TreeNode* root) {
        return help(root,LONG_MIN,LONG_MAX);
    }
private:
    bool help(TreeNode *root, long lower,long upper){
        if(!root)   return true;
        if(root->val<=lower||root->val>=upper)  return false;
        return help(root->left,lower,root->val)&&help(root->right,root->val,upper);
    }
};
```

3. 中序遍历
> 根据二叉搜索树的性质，中序遍历序列递增

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
    bool isValidBST(TreeNode* root) {
        if(!root)   return true;
        stack<TreeNode*> st;
        int pre=INT_MIN;    // 记录前一个数
        int count=0;    // 记录当前遍历数量，特殊处理第一个
        while(root||!st.empty()){
            while(root){
                st.push(root);
                root=root->left;
            }
            if(!st.empty()){
                if(count>0&&st.top()->val<=pre) return false;
                pre=st.top()->val;
                ++count;
                root=st.top()->right;
                st.pop();  
            }
        }
        return true;
    }
};
```