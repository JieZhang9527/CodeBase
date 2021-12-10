1. 层序遍历
> 从上到下层序遍历二叉树，更新每个节点的值为根节点到当前节点的路径和。缺点是需要修改二叉树

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
    bool hasPathSum(TreeNode* root, int sum) {
        if(!root)   return false;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            int count=q.size();
            for(int i=0;i<count;++i){
                auto temp=q.front();
                q.pop();
                if(!temp->left&&!temp->right&&temp->val==sum)   return true;
                if(temp->left){
                    temp->left->val+=temp->val;
                    q.push(temp->left);
                }
                if(temp->right){
                    temp->right->val+=temp->val;
                    q.push(temp->right);
                }
            }
        }
        return false;
    }
};
```

2. 递归

```C++
class Solution {
public:
    bool hasPathSum(TreeNode* root, int sum) {
        if(!root)   return false;
        if(!root->left&&!root->right&&root->val==sum)   return true;
        if(hasPathSum(root->left,sum-root->val)||hasPathSum(root->right,sum-root->val))
            return true;
        return false;
    }
};
```

3. DFS
> 先序深度优先遍历

```C++
class Solution {
public:
    bool hasPathSum(TreeNode* root, int sum) {
        if(!root)   return false;
        stack<pair<TreeNode*,int>> st;
        st.push(make_pair(root,root->val));
        while(!st.empty()){
            TreeNode *node=st.top().first;
            int num=st.top().second;
            st.pop();
            if(!node->left&&!node->right){
                if(num==sum) return true;
            }
            if(node->left)  st.push(make_pair(node->left,num+node->left->val));
            if(node->right) st.push(make_pair(node->right,num+node->right->val));
        }
        return false;
    }
};
```