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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> ans;
        if(!root)   return ans;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            vector<int> nums;
            int count=q.size();
            for(int i=0;i<count;++i){
                auto temp=q.front();
                q.pop();
                nums.push_back(temp->val);
                if(temp->left)  q.push(temp->left);
                if(temp->right) q.push(temp->right);
            }
            ans.push_back(nums);
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};
```