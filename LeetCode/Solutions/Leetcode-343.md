1. dp

> dp[i]表示整数i可以拆分的最大乘积，关键是动态转移方程，分别计算$j*dp[i-j]$和$j*(i-j)$的原因是既要计算分解为两个的情形也要计算分解为多个整数的情形

```C++
class Solution {
public:
    int integerBreak(int n) {
        vector<int> dp(n+1,0);
        dp[2]=1;
        for(int i=3;i<=n;++i){
            for(int j=1;j<i;++j){
                // 要考虑到两个数相乘和多个数相乘
                dp[i]=max(dp[i],max(j*dp[i-j],j*(i-j)));
            }
        }
        return dp.back();
    }
};
```