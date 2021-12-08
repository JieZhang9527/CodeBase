1. 层序遍历

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
    int findBottomLeftValue(TreeNode* root) {
        int ans=0;
        TreeNode *temp=root;
        queue<TreeNode*> q;
        q.push(temp);
        while(!q.empty()){
            int count=q.size();
            ans=q.front()->val;
            for(int i=0;i<count;++i){
                temp=q.front();
                q.pop();
                if(temp->left)  q.push(temp->left);
                if(temp->right) q.push(temp->right);
            }
        }
        return ans;
    }
};
```

2. 反向层序遍历

> 先入队右子树再入队左子树，使得最后一个访问的值就是左下角的值

```C++
class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        int ans=0;
        TreeNode *temp=root;
        queue<TreeNode*> q;
        q.push(temp);
        while(!q.empty()){
            temp=q.front();
            q.pop();
            ans=temp->val;
            if(temp->right) q.push(temp->right);
            if(temp->left)  q.push(temp->left);
        }
        return ans;
    }
};
```