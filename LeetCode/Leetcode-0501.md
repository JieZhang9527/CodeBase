1. 中序非递归

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
    vector<int> findMode(TreeNode* root) {
        return inOrder(root);
    }
private:
    vector<int> inOrder(TreeNode *root){
        vector<int> ans;
        if(!root)   return ans;
        stack<TreeNode *> st;
        int pre=root->val;
        int current=0, count=0;
        while(!st.empty()||root){
            while(root){
                st.push(root);
                root=root->left;
            }
            if(!st.empty()){
                auto temp=st.top();  st.pop();
                if(temp->val==pre)  ++current;
                else{
                    if(current>=count){
                        if(current>count)   ans.clear();
                        ans.push_back(pre);
                        count=current;
                    }
                    current=1;
                }
                pre=temp->val;
                root=temp->right;
            }
        }
        if(current>=count){
            if(current>count)   ans.clear();
            ans.push_back(pre);
        }
        return ans;
    }
};
```