1. 回溯
> 相同的去重方式

```C++
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> ans;
        if(nums.empty())    return ans;
        sort(nums.begin(),nums.end());  // 排序是去重的前提
        vector<bool> visited(nums.size(),false);
        vector<int> path;
        DFS(nums,path,visited,ans);
        return ans;
    }
    void DFS(vector<int>&nums,vector<int>&path,vector<bool>&visited,vector<vector<int>> &ans){
        if(path.size()==nums.size()){
            ans.push_back(path);
            return;
        }
        for(int i=0;i<nums.size();++i){
            // 去除重复
            if(visited[i]||(i>0&&nums[i]==nums[i-1]&&visited[i-1])) continue;
            path.push_back(nums[i]);
            visited[i]=true;
            DFS(nums,path,visited,ans);
            path.pop_back();
            visited[i]=false;
        }
    }
};
```