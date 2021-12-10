1. dp
> dp[i][j] 表示[0,i]天状态为j时的最大收益，和只能买卖两次本质上方法差不多

```C++
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        if(prices.size()<2||k==0)   return 0;
        vector<vector<int>> dp(prices.size(), vector<int>(2*k+1,0));
        dp[0][0]=0; dp[0][1]=-prices[0];
        for(int i=0;i<prices.size();++i){
            for(int j=2;j<2*k+1;++j){
                dp[i][j]=INT_MIN;
            }
        }
        int depth=0;
        for(int i=1;i<prices.size();++i){
            for(int j=1;j<2*k+1;++j){
                if(depth%2==0)
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1]-prices[i]);
                else
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1]+prices[i]);
                ++depth;
            }
        }
        int ans=0;
        for(int i=0;i<2*k+1;++i){
            if(i%2==0)  ans=max(ans,dp.back()[i]);
        }
        return ans;
    }
};
```