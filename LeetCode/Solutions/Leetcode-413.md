1. dp

> dp[i]表示到索引为i的数字的最长等差数列长度  
> 初始化：dp[0]=1,dp[1]=2;  
> 如果当前数字不是前面等差数列的一部分，重新开始等差数列dp[i]=2;  
> 如果是前面等差数列的一部分，dp[i]=dp[i-1]+1  

```C++
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        if(A.size()<3)  return 0;
        vector<int> dp(A.size(),0);
        dp[0]=1; dp[1]=2;
        int ans=0;
        for(int i=2;i<A.size();++i){
            if(A[i]-A[i-1]==A[i-1]-A[i-2])  dp[i]=dp[i-1]+1;
            else{
                dp[i]=2;
                ans+=help(dp[i-1]);
            }
        }
        ans+=help(dp.back());
        return ans;
    }
private:
    // 记录长度为len的连续等差数列包含的等差数列的个数
    int help(int len){
        int ans=0;
        for(int i=1;i<=len-2;++i)   ans+=i;
        return ans;
    }
};
```