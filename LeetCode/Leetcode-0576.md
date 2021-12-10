1. dp

> dp[i][j][k] 表示从(i,j)出发第K步出界的路径数，等价于从外界出发第K步走到(i,j)的路径数  
> 状态转移方程：  
dp[i][j][k]=dp[i−1][j][k−1]+dp[i+1][j][k−1]+dp[i][j−1][k−1]+dp[i][j+1][k−1]  

> 注意将外界的初始值设定为1

```C++
class Solution {
public:
    int findPaths(int m, int n, int N, int i, int j) {
        const int MOD=1e9+7;
        if(N==0)    return 0;
        vector<vector<vector<int>>> dp(m+2,vector<vector<int>>(n+2,vector<int>(N+1,0)));
        for(int i=0;i<m+2;++i){
            dp[i][0][0]=1;
            dp[i][n+1][0]=1;
        }
        for(int j=0;j<n+2;++j){
            dp[0][j][0]=1;
            dp[m+1][j][0]=1;
        }
        for(int k=1;k<=N;++k){
            for(int i=1;i<=m;++i){
                for(int j=1;j<=n;++j){
                    dp[i][j][k]=((dp[i-1][j][k-1]+dp[i+1][j][k-1])%MOD+(dp[i][j-1][k-1]+dp[i][j+1][k-1])%MOD)%MOD;
                }
            }
        }
        int ans=0;
        for(int k=1;k<=N;++k){
            ans=(ans+dp[i+1][j+1][k])%MOD;
        }
        return ans;
    }
};
```