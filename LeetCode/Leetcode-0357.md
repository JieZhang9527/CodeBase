1. 找规律

> 计算n位数的各位数字都不相同的个数：  
> 第一位有9种选择（除去0），第二位有（10-1）种选择，第三位有（10-1-1）种选择$\cdots$第n位有（10-n+1）种选择  
> 前提是 n>=2，因此 n=0,n=1需要单独判断

```C++
class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        if(n==0)    return 1;
        if(n==1)    return 10;
        vector<int> dp(n+1,0);
        dp[0]=1;
        dp[1]=9;
        int ans=dp[0]+dp[1];
        for(int i=2;i<=n;++i){
            dp[i]=dp[i-1]*(11-i);
            ans+=dp[i];
        }
        return ans;
    }
};
```