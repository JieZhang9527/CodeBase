> 本质上是寻找两个字符串的最长不连续公共子串

> dp[i][j]表示word1[:i-1] word2[:j-1]的最长不连续公共子串。表示的是前i个字符和前j个字符!!!!  
> 初始化：dp[0][j]=0,dp[i][0]=0;

> 为什么二维dp数组的宽度和长度要比两个字符串的长度多1？  
> 如果不这么做，第一行和第一列求解结点的左上方就没有结点，就要额外判断

```C++
class Solution {
public:
    int minDistance(string word1, string word2) {
        vector<vector<int>> dp(word1.size(),vector<int>(word2.size(),0));
        for(int i=0;i<word1.size();++i){
            for(int j=0;j<word2.size();++j){
                if(i==0||j==0){
                    if(i==0&&j==0&&word1[i]==word2[j])  dp[i][j]=1;
                    
                }
                if(word1[i-1]==word2[j-1])
                    dp[i][j]=dp[i-1][j-1]+1;
                else
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1]);
            }
        }
        int ans=word1.size()+word2.size()-2*dp[word1.size()][word2.size()];
        return ans;
    }
};
```