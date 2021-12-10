1. dp
> dp[i-1]表示第i个丑数，每个丑数都是前面丑数的2，3，5倍，取其最小值作为新的丑数

```C++
class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> dp(n,0);
        // 特殊条件判断，第一个丑数是1
        dp[0]=1;
        // 表示生成当前数的索引
        int p2=0, p3=0, p5=0;
        for(int i=1;i<n;++i){
            int min_val=min(dp[p2]*2,min(dp[p3]*3,dp[p5]*5));
            dp[i]=min_val;
            if(min_val==dp[p2]*2)   ++p2;
            if(min_val==dp[p3]*3)   ++p3;
            if(min_val==dp[p5]*5)   ++p5;
        }
        return dp.back();
    }
};
```