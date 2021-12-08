1. 后序遍历非递归

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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ans;
        stack<TreeNode*> st;
        unordered_set<TreeNode*> ust;   // 哈希记录节点的右子树是否已被访问
        while(root||!st.empty()){
            while(root){
                st.push(root);
                root=root->left;
            }
            // 右子树已被访问过
            while(!st.empty()&&ust.find(st.top())!=ust.end()){
                ans.push_back(st.top()->val);
                st.pop();
            }
            if(!st.empty()){
                root=st.top()->right;
                ust.insert(st.top());
            }
        }
        return ans;
    }
};
```

2. 先序遍历改为后序遍历
> 后序遍历左右根，先序遍历改为根右左，反转后即可得到后序遍历结果

```C++
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ans;
        stack<TreeNode*> st;
        while(root||!st.empty()){
            while(root){
                st.push(root);
                ans.push_back(root->val);
                root=root->right;
            }
            if(!st.empty()){
                root=st.top()->left;
                st.pop();
            }
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};
```