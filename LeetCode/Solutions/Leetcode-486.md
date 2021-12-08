1. dp

> dp[i][j]表示在当前数为nums[i……j]，当前操作的人比接下来操作的另一个人多得的分数  
> 初始化：dp[i][i]=nums[i]  
> 状态转移方程：dp[i][j]=max(nums[i]-dp[i+1][j],nums[j]-dp[i][j-1])  

```C++
class Solution {
public:
    bool PredictTheWinner(vector<int>& nums) {
        vector<vector<int>> dp(nums.size(),vector<int>(nums.size(),0));
        for(int i=0;i<nums.size();++i)  dp[i][i]=nums[i];
        for(int len=1;len<nums.size();++len){
            for(int i=0,j=len;j<nums.size();++i,++j){
                dp[i][j]=max(nums[i]-dp[i+1][j],nums[j]-dp[i][j-1]);
            }
        }
        return dp[0][nums.size()-1]>=0;
    }
};
```