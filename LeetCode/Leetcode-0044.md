1. dp
> 相同的思路

```C++
class Solution {
public:
    bool isMatch(string s, string p) {
        vector<vector<bool>> dp(s.size()+1,vector<bool>(p.size()+1,false));
        for(int i=0;i<=s.size();++i){
            for(int j=0;j<=p.size();++j){
                // 模式串为空串时，只有字符串为空方可匹配
                if(j==0)    dp[i][j]=(i==0);
                else{
                    if(p[j-1]!='*'){
                        if(i>0&&(s[i-1]==p[j-1]||p[j-1]=='?'))
                            dp[i][j]=dp[i-1][j-1];
                    }
                    else{
                        // 不看"*"
                        if(j>0) dp[i][j]=dp[i][j]||dp[i][j-1];
                        // 看"*"
                        if(i>0) dp[i][j]=dp[i][j]||dp[i-1][j];
                    }
                }
            }
        }
        return dp.back().back();
    }
};
```