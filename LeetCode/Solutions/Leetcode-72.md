1. dp
> dp[i][j] 是指将 word1[0,i) 变换到 word2[0,j) 的最少操作数。其中，dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作
> - 如果word1[i] == word2[j], dp[i][j] = dp[i-1][j-1]
> - 如果word1[i] != word2[j]，dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1  

```C++
class Solution {
public:
    int minDistance(string word1, string word2) {
        vector<vector<int>> dp(word1.size()+1,vector<int>(word2.size()+1,0));
        for(int i=0;i<=word1.size();++i)    dp[i][0]=i;
        for(int i=0;i<=word2.size();++i)    dp[0][i]=i;
        for(int i=1;i<=word1.size();++i){
            for(int j=1;j<=word2.size();++j){
                // i-1 和 j-1
                if(word1[i-1]==word2[j-1])  dp[i][j]=dp[i-1][j-1];
                else    dp[i][j]=min(dp[i-1][j-1],min(dp[i-1][j],dp[i][j-1]))+1;
            }
        }
        return dp.back().back();
    }
};
```