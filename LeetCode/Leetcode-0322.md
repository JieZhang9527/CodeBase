1. dp

> dp[i]表示组成数额i的最少硬币数

```C++
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount+1,amount+1);
        dp[0]=0;
        for(int i=1;i<=amount;++i) {
            for(auto coin : coins){
                if(i-coin>=0)   dp[i]=min(dp[i],dp[i-coin]+1);
            }
        }
        return dp.back()==amount+1?-1:dp.back();
    }
};
```