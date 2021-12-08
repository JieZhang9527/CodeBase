1. 非递归中序遍历

```C++
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        return inOrder(root,k);
    }
private:
    int inOrder(TreeNode *root, int k){
        if(!root)   return -1;
        stack<TreeNode*> st;
        while(root||!st.empty()){
            while(root){
                st.push(root);
                root=root->left;
            }
            if(!st.empty()){
                auto temp=st.top();
                st.pop();
                --k;
                if(k==0)    return temp->val;
                root=temp->right;
            }
        }
        return -1;
    }
};
```