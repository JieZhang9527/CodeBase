1. DFS 

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
    vector<int> findFrequentTreeSum(TreeNode* root) {
        int count=0;    // 记录出现次数最多子树和出现的次数
        unordered_map<int,int> ump;
        DFS(root,ump,count);
        vector<int> ans;
        for(auto it : ump){
            if(it.second==count)    ans.push_back(it.first);
        }
        return ans;
    }
private:
    int DFS(TreeNode *root, unordered_map<int,int> &ump, int &count){
        if(!root)   return 0;
        root->val+=DFS(root->left,ump,count)+DFS(root->right,ump,count);
        ump[root->val]++;
        count=max(count,ump[root->val]);
        return root->val;
    }
};
```