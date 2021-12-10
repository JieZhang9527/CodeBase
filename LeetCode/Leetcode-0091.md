1. dp
> dp[i]表示结尾为s[i]字符串的译码数  
> - 初始化，如果s[0]='0'，无法译码，直接返回0，否则s[0]=1
> - 遍历第i个字符，如果s[i]='0'，只能和前一个一起译码。如果s[i-1]=='1'||s[i-1]=='2'，dp[i]=dp[i-1]。否则无法译码直接返回0
> - 如果s[i-1]=='1'||(s[i-1]=='2'&&s[i]>='0'&&s[i]<='6') dp[i]=dp[i-2]+dp[i-1]，否则dp[i]=dp[i-1]

```C++
class Solution {
public:
    int numDecodings(string s) {
        if(s.size()==0||s[0]=='0') return 0;
        vector<int> dp(s.size(),0);
        dp[0]=1;
        for(int i=1;i<s.size();++i){
            if(s[i]=='0'){
                if(s[i-1]=='1'||s[i-1]=='2'){
                    if(i-2>=0)  dp[i]=dp[i-2];
                    else    dp[i]=1;
                }
                else    return 0;
            }
            else if(s[i-1]=='1'||(s[i-1]=='2'&&s[i]>='0'&&s[i]<='6')){
                if(i-2>=0)  
                    dp[i]=dp[i-1]+dp[i-2];
                else
                    dp[i]=dp[i-1]+1;
            }
            else 
                dp[i]=dp[i-1];
        }
        return dp.back();
    }
};
```