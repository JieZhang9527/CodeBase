1. dp

> dp[i]表示总金额为i时，组合数  
> 从没有硬币开始，一一添加硬币，对于每个添加的硬币，计算可以得到那些金额。

```C++
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<int> dp(amount+1,0);
        dp[0]=1;
        for(auto coin : coins){
            for(int i=coin;i<=amount;++i){
                dp[i]+=dp[i-coin];
            }
        }
        return dp.back();
    }
};
```