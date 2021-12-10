1. dp

> 假设有目标序列 2 4 8 若此时x是8的倍数，那么一定可以添加到目标序列，这样就将一个大问题分解为小的问题  
> dp[i] nums[i]结尾的目标序列的最大长度
> path[i] 以nums[i]结尾的目标序列的上一个元素的下标（用来记录路径）  
> 状态转移：对每个元素x,遍历在他之前的所有元素y，如果x是y的倍数，是一个目标序列，获取满足这种情况的最长目标序列，记录对应y的下标

```C++
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        if(nums.empty())    return vector<int>();    
        vector<int> dp(nums.size(),1), path(nums.size(),-1);
        sort(nums.begin(),nums.end());
        // 记录最大整除子集的长度和对应的终点索引
        int max_count=1, end_index=0;
        for(int i=1;i<nums.size();++i){
            for(int j=0;j<i;++j){
                if(nums[i]%nums[j]==0&&dp[j]+1>dp[i]){
                    dp[i]=dp[j]+1;
                    path[i]=j;
                }
            }
            if(dp[i]>max_count){
                max_count=dp[i];
                end_index=i;
            }
        }
        vector<int> ans;
        for(int i=end_index;i!=-1;i=path[i])    ans.push_back(nums[i]);
        return ans;
    }
};
```