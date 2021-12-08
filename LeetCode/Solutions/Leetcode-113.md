1. DFS 
> 注意path类型为引用，因此在最后要去除该元素

```C++
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<int> path;
        vector<vector<int>> ans;
        DFS(root,sum,path,ans);
        return ans;
    }
private:
    void DFS(TreeNode *root, int sum, vector<int> &path, vector<vector<int>> &ans){
        if(!root)   return;
        path.push_back(root->val);
        sum-=root->val;
        if(!root->left&&!root->right&&sum==0)   ans.push_back(path);
        DFS(root->left,sum,path,ans);
        DFS(root->right,sum,path,ans);
        // 当前层用完要丢弃
        path.pop_back();
    }
};
```