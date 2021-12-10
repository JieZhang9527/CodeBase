1. dp
> dp[i][j]表示s1的前i个字符和s2的j个字符能否构成s3的i+j个字符

```C++
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        if(s1.empty())  return s2==s3;
        if(s2.empty())  return s1==s3;
        if(s1.size()+s2.size()!=s3.size())  return false;
        vector<vector<bool>> dp(s1.size()+1,vector<bool>(s2.size()+1,false));
        dp[0][0]=true;
        for(int i=1;i<=s1.size();++i){
            if(s1[i-1]==s3[i-1])    dp[i][0]=true;
            else    break;
        }
        for(int j=1;j<=s2.size();++j){
            if(s2[j-1]==s3[j-1])    dp[0][j]=true;
            else    break;
        }
        for(int i=1;i<=s1.size();++i){
            for(int j=1;j<=s2.size();++j){
                char c=s3[i+j-1];
                dp[i][j]=(dp[i-1][j]&&s1[i-1]==c)||(dp[i][j-1]&&s2[j-1]==c);
            }
        }
        return dp.back().back();
    }
};
```