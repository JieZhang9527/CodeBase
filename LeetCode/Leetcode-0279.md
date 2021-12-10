1. dp

> 令dp[i]表示组成i的完全平方数的最小个数，初始dp[i]=i

```C++
class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n+1,0);
        for(int i=1;i<=n;++i){
            dp[i]=i;
            for(int j=1;j*j<=i;++j){
                dp[i]=min(dp[i],dp[i-j*j]+1);
            }
        }
        return dp.back();
    }
};
```