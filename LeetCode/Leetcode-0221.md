1. dp

> 注意这里是求得面积最大的正方形而不是最大的矩形

> dp[i][j]表示以[i][j]为右下角的正方形的边长  
> 如果matrix[i][j]=='0' 那么不是正方形，dp[i][j]=0;  
> 如果matrix[i][j]=='1' 
> dp[i][j]=min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1，可以画图示意

```C++
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if(matrix.empty()||matrix[0].empty())   return 0;
        int rows=matrix.size(), cols=matrix[0].size();
        vector<vector<int>> dp(rows,vector<int>(cols,0));
        int ans=0;
        for(int i=0;i<rows;++i){
            dp[i][0]=matrix[i][0]=='0'?0:1;
            if(dp[i][0]==1) ans=1;
        }
        for(int j=0;j<cols;++j){
            dp[0][j]=matrix[0][j]=='0'?0:1;
            if(dp[0][j])    ans=1;
        }
        for(int i=1;i<rows;++i){
            for(int j=1;j<cols;++j){
                if(matrix[i][j]=='0')   continue;
                dp[i][j]=min(dp[i-1][j-1],min(dp[i-1][j],dp[i][j-1]))+1;
                ans=max(ans,dp[i][j]);
            }
        }
        return pow(ans,2);
    }
};
```