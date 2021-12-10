1. dp
   
> 为了解决上述问题，我们从左上角和右下角两次遍历，左上角遍历解决左上，右下角开始的遍历解决右下。

```C++
class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        if(matrix.empty()||matrix[0].empty()) return {};
        int rows=matrix.size(),cols=matrix[0].size();
        vector<vector<int>> dp(rows,vector<int>(cols,INT_MAX-10000));
        for(int i=0;i<rows;++i){
            for(int j=0;j<cols;++j){
                if(matrix[i][j]==0) dp[i][j]=0;
                else{
                    if(i>0) dp[i][j]=min(dp[i][j],dp[i-1][j]+1);
                    if(j>0) dp[i][j]=min(dp[i][j],dp[i][j-1]+1);
                }
            }
        }
        for(int i=rows-1;i>=0;--i){
            for(int j=cols-1;j>=0;--j){
                if(i<rows-1) dp[i][j]=min(dp[i][j],dp[i+1][j]+1);
                if(j<cols-1) dp[i][j]=min(dp[i][j],dp[i][j+1]+1);
            }
        }
        return dp;
    }
};
```