1. dp

> dp[i]表示组合为数字i的方案数

```C++
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<int> dp(target+1,0);
        dp[0]=1;
        for(int i=1;i<=target;++i){
            for(auto num : nums){
                if(i-num>=0)    dp[i]+=dp[i-num];
            }
        }
        return dp.back();
    }
};
```