1. dp

```C++
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if(nums.empty())    return 0;
        vector<int> dp(nums.size(),0);
        dp[0]=nums[0];
        int ans=dp[0];
        for(int i=1;i<nums.size();++i){
            dp[i]=max(dp[i-1]+nums[i],nums[i]);
            ans=max(ans,dp[i]);
        }
        return ans;
    }
};
```