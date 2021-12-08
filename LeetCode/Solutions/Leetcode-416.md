1. 0-1背包问题

> dp[i][j]表示前i个元素能否组成元素j  
> 如果不选当前元素：dp[i][j]=dp[i-1][j]，如果选择当前元素：dp[i][j]=dp[i-1][j-num]

```C++
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum=accumulate(nums.begin(),nums.end(),0);
        if(sum%2==1)    return false;
        int target=sum/2;
        vector<vector<bool>> dp(nums.size(),vector<bool>(target+1,false));
        for(int i=0;i<nums.size();++i)  dp[i][0]=true;
        for(int i=1;i<nums.size();++i){
            for(int j=1;j<=target;++j){
                if(dp[i-1][j]||(j-nums[i]>=0&&dp[i-1][j-nums[i]]))
                    dp[i][j]=true;
            }
        }
        return dp.back().back();
    }
};
```