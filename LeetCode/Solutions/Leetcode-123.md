1. dp
> 有限状态机，某个状态可以由另一个状态转换而来，状态定义：dp[i][j]表示区间[0,i]内状态为j的最大收益，其中：  
> j=0: 还未开始交易  
> j=1: 第一次买入股票  
> j=2: 第一次卖出股票  
> j=3: 第二次买入股票  
> j=4: 第二次卖出股票  

> 状态转移：状态要么停留，要么向前走，不能回退

```C++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size()<2) return 0;
        vector<vector<int>> dp(prices.size(),vector<int>(5,INT_MIN));
        dp[0][0]=0;
        dp[0][1]=-prices[0];
        for(int i=1;i<prices.size();++i){
            dp[i][0]=0;
            dp[i][1]=max(dp[i-1][1],dp[i][0]-prices[i]);
            dp[i][2]=max(dp[i-1][2],dp[i][1]+prices[i]);
            dp[i][3]=max(dp[i-1][3],dp[i][2]-prices[i]);
            dp[i][4]=max(dp[i-1][4],dp[i][3]+prices[i]);
        }
        return dp.back()[4];
    }
};
```
