1. dp
> 因为需要记录空串时的状态，所以dp[i][j]表示字符串s[0,i)和模式串p[0,j) 是否能够匹配  
> 初始化：  
> 如果字符串的长度为0，模式串的长度为非0，则需要判断  
> 如果模式串的长度为0，字符串的长度为非0，则一定不匹配  
> 状态转移方程：  
> - 如果p[j]是字符，那么直接比较这两个字符
> - 如果p[j]是'.', 可以匹配任意字符，直接看各自的前一个字符
> - 如果p[j]是'*'：
>   - 前一个字符重复0次，因此去除模式串最后两个字符
>   - 前一个字符重复数次，去除字符串的最后一次字符后继续比较

```C++
class Solution {
public:
    bool isMatch(string s, string p) {
        vector<vector<bool>> dp(s.size()+1,vector<bool>(p.size()+1,false));
        for(int i=0;i<=s.size();++i){
            for(int j=0;j<=p.size();++j){
                if(j==0)    dp[i][j]=(i==0);
                else{
                    if(p[j-1]!='*'){
                        if(i>0&&(s[i-1]==p[j-1]||p[j-1]=='.'))
                            dp[i][j]=dp[i-1][j-1];
                    }
                    else{
                        if(j>=2) dp[i][j]=dp[i][j]||dp[i][j-2];
                        if(i>=1&&j>=2&&(s[i-1]==p[j-2]||p[j-2]=='.'))
                            dp[i][j]=dp[i][j]||dp[i-1][j];
                    }
                }
            }
        }
        return dp.back().back();
    }
};
```