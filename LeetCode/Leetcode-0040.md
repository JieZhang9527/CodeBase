1. 回溯
   
```C++
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        vector<int> temp;
        sort(candidates.begin(),candidates.end());
        DFS(candidates,0,target,temp,ans);
        return ans;
    }
private:
    void DFS(vector<int> &candidates,int start,int target,vector<int> &temp,vector<vector<int>> &ans){
        if(target==0){
            ans.push_back(temp);
            return;
        }
        // 剪枝包含在for循环中
        for(int i=start;i<candidates.size()&&candidates[i]<=target;++i){
            // 去除重复
            if(i>start&&candidates[i]==candidates[i-1]) continue;
            temp.push_back(candidates[i]);
            // 每个元素只有一次选择机会，所以i+1
            DFS(candidates,i+1,target-candidates[i],temp,ans);
            temp.pop_back();
        }
    }
};
```