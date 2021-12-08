1. dp

> dp[i][j]表示索引i,j之间的数组的最长回文子序列

```C++
class Solution {
public:
    int longestPalindromeSubseq(string s) {
        vector<vector<int>> dp(s.size(),vector<int>(s.size(),0));
        for(int i=0;i<s.size();++i)  dp[i][i]=1;
        for(int len=1;len<s.size();++len){
            for(int i=0;i+len<s.size();++i){
                int j=i+len;
                if(s[i]==s[j])
                    dp[i][j]=dp[i+1][j-1]+2;
                else    
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1]);
            }
        }
        return dp[0][s.size()-1];
    }
};
```