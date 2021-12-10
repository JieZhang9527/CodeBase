1. dp
> 首尾不能同时取，可以简化为以下两种情况
> - 一次从头开始不能选尾
> - 一次头不能取，尾可以取

```C++
class Solution {
public:
    int rob(vector<int>& nums) {
        //必须单独判断，否则交错判断返回0
        if(nums.size()==1)  return nums[0];
        int select_start=helper(nums,0,nums.size()-2);
        int no_select_start=helper(nums,1,nums.size()-1);
        return max(select_start,no_select_start);
    }
    int helper(vector<int> &nums,int left,int right){
        if(left>right) return 0;
        vector<int> dp(right-left+1,0);
        int index=0;
        dp[index++]=nums[left];
        if(left<right)  dp[index++]=max(nums[left],nums[left+1]);
        for(int i=left+2;i<=right;++i){
            dp[index]=max(dp[index-1],dp[index-2]+nums[i]);
            ++index;
        }
        return dp.back();
    }
};
```