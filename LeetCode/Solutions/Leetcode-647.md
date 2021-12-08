1. dp

> dp[i][j]表示[i,j]之间是不是回文串  
> 状态转移方程：  
> ```
> if s[i]==s[j]&&dp[i+1][j-1]  dp[i][j]=1;  
> else  dp[i][j]=0;
> ```

```C++
class Solution {
public:
    int countSubstrings(string s) {
        if(s.empty()||s.size()==1)   return s.size();
        vector<vector<bool>> dp(s.size(),vector<bool>(s.size(),true));
        int ans=s.size();
        for(int len=1;len<s.size();++len){
            for(int i=0,j=i+len;j<s.size();++i,++j){
                if(s[i]==s[j]&&dp[i+1][j-1]){
                    dp[i][j]=true;
                    ++ans;
                }
                else dp[i][j]=false;
            }
        }
        return ans;
    }
};
```

1. 中心拓展算法

```C++
class Solution {
public:
    int countSubstrings(string s) {
        int ans=0;
        for(int i=0;i<s.size();++i){
            ans+=expandAroundCenter(s,i,i);
            ans+=expandAroundCenter(s,i,i+1);
        }
        return ans;
    }
    int expandAroundCenter(const string &s,int left,int right){
        int ans=0;
        while(left>=0&&right<s.size()&&s[left]==s[right]){
            ++ans;
            --left;
            ++right;
        }
        return ans;
    }
};
```