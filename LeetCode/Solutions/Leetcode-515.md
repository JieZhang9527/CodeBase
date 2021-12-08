1. 层序遍历

```C++
class Solution {
public:
    vector<int> largestValues(TreeNode* root) {
        return levelOrder(root);
    }
    vector<int> levelOrder(TreeNode *root){
        vector<int> ans;
        if(!root)   return ans;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            int count=q.size();
            int max_value=INT_MIN;
            for(int i=0;i<count;++i){
                root=q.front();
                q.pop();
                max_value=max(max_value,root->val);
                if(root->left)  q.push(root->left);
                if(root->right) q.push(root->right);
            }
            ans.push_back(max_value);
        }
        return ans;
    }
};
```