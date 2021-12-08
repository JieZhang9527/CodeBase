1. dp
> dp[i][j]表示在点(i,j)需要的最少生命值，注意公主在矩阵之外，所以需要分别加一行一列，从右下角往左上角走

```C++
class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        if(dungeon.empty()||dungeon[0].empty()) return 0;
        int rows=dungeon.size(), cols=dungeon[0].size();
        vector<vector<int>> dp(rows+1,vector<int>(cols+1,INT_MAX));
        dp[rows][cols-1]=dp[rows-1][cols]=1;
        for(int i=rows-1;i>=0;--i){
            for(int j=cols-1;j>=0;--j){
                int temp=min(dp[i+1][j],dp[i][j+1]);
                dp[i][j]=max(temp-dungeon[i][j],1);
            }
        }
        return dp[0][0];
    }
};
```