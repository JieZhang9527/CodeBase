1. 保存和矩阵

```C++
class NumMatrix {
public:
    NumMatrix(vector<vector<int>>& matrix) {
        if(matrix.size()==0||matrix[0].size()==0)   return;
        dp=matrix;
        int rows=matrix.size(),cols=matrix[0].size();
        for(int i=1;i<rows;++i) dp[i][0]=dp[i-1][0]+matrix[i][0];
        for(int j=1;j<cols;++j) dp[0][j]=dp[0][j-1]+matrix[0][j];
        for(int i=1;i<rows;++i){
            for(int j=1;j<cols;++j){
                dp[i][j]=dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+matrix[i][j];
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        int ans=dp[row2][col2];
        if(col1-1>=0)   ans-=dp[row2][col1-1];
        if(row1-1>=0)   ans-=dp[row1-1][col2];
        if(row1-1>=0&&col1-1>=0)    ans+=dp[row1-1][col1-1];
        return ans;
    }
private:
    vector<vector<int>> dp;
};
```