1. 二叉搜索树中序遍历

```C++
class Solution {
public:
    int getMinimumDifference(TreeNode* root) {
        if(!root)   return 0;
        stack<TreeNode*> st;
        TreeNode *pre=root;
        int ans=INT_MAX;
        while(root||!st.empty()){
            while(root){
                st.push(root);
                root=root->left;
            }
            if(!st.empty()){
                auto temp=st.top();
                st.pop();
                if(temp!=pre)   ans=min(ans,abs(temp->val-pre->val));
                pre=temp;
                root=temp->right;
            }
        }
        return ans;
    }
};
```