1. 回溯
> 每个数有选和不选两种，回溯的优化主要是剪枝提前退出

```C++
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        vector<int> temp;
        // 排序是剪枝的基础
        sort(candidates.begin(),candidates.end());
        DFS(candidates,0,target,temp,ans);
        return ans;
    }
    void DFS(vector<int> &candidates,int start,int target,vector<int> &temp,vector<vector<int>> &ans){
        if(target==0){
            ans.push_back(temp);
            return;
        }
        for(int i=start;i<candidates.size();++i){
            // 剪枝
            if(target<candidates[i])    break;
            temp.push_back(candidates[i]);
            DFS(candidates,i,target-candidates[i],temp,ans);
            temp.pop_back();
        }
    }
};
```