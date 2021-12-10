1. 回溯

```C++
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> temp;
        vector<vector<int>> ans;
        for(int len=0;len<=nums.size();++len){
            DFS(0,len,nums,temp,ans);
        }
        return ans;
    }
private:
    void DFS(int curr, int len, vector<int> &nums, vector<int> temp,vector<vector<int>> &ans){
        if(temp.size()==len){
            ans.push_back(temp);
            return;
        }
        for(int i=curr;i<nums.size();++i){
            temp.push_back(nums[i]);
            DFS(i+1,len,nums,temp,ans);
            temp.pop_back();
        }
    }
};
```

2. 循环求解
> 假设nums=[1,2,3]，初始化ans,空集是所有集合的子集；对于ans中的每个集合加入当前遍历的数字  
> {{}}  
> {{},{1}}  
> {{},{1},{2},{1,2}} 
> {{},{1},{2},{1,2},{3},{1,3},{2,3},{1,2,3}}
```C++
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans={{}};
        for(auto num : nums){
            int count=ans.size();
            for(int i=0;i<count;++i){
                auto temp=ans[i];
                temp.push_back(num);
                ans.push_back(temp);
            }
        }
        return ans;
    }
};
```