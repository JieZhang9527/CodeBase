1. dp

```C++
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid){
        int rows=obstacleGrid.size(), cols=obstacleGrid[0].size();
        vector<vector<int>> dp(rows,vector<int>(cols,0));
        bool hasObstacle=false;
        for(int i=0;i<rows;++i){
            if(obstacleGrid[i][0]==1)   hasObstacle=true;
            if(hasObstacle) dp[i][0]=0;
            else    dp[i][0]=1;   
        }
        hasObstacle=false;
        for(int j=0;j<cols;++j){
            if(obstacleGrid[0][j])  hasObstacle=true;
            if(hasObstacle) dp[0][j]=0;
            else    dp[0][j]=1;
        }
        for(int i=1;i<rows;++i){
            for(int j=1;j<cols;++j){
                if(obstacleGrid[i][j])   dp[i][j]=0;
                else    dp[i][j]=dp[i-1][j]+dp[i][j-1];
            }
        }
        return dp[rows-1][cols-1];
    }
};
```