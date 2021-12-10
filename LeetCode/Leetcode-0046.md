1. 回溯

```C++
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        if(nums.empty())    return ans;
        vector<bool> visited(nums.size(),false);
        vector<int> path;
        DFS(nums,path,visited,ans);
        return ans;
    }
    void DFS(vector<int> &nums,vector<int> &path,vector<bool>&visited,vector<vector<int>>&ans){
        if(path.size()==nums.size()){
            ans.push_back(path);
            return;
        }
        for(int i=0;i<nums.size();++i){
            if(visited[i])  continue;
            path.push_back(nums[i]);
            visited[i]=true;
            DFS(nums,path,visited,ans);
            path.pop_back();
            visited[i]=false;
        }
    }
};
```