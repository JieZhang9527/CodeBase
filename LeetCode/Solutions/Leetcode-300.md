1. dp

> dp[i]表示以i结尾的最长上升子序列的长度，注意本题中不要求序列连续

```C++
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if(nums.empty())    return 0;
        vector<int> dp(nums.size(),1);
        int ans=1;
        for(int i=1;i<nums.size();++i){
            for(int j=i-1;j>=0;--j){
                if(nums[i]>nums[j]) dp[i]=max(dp[i],dp[j]+1);
            }
            ans=max(ans,dp[i]);
        }
        return ans;
    }
};
```