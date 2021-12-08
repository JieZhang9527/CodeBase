1. dp
> 动态规划算法，dp[i][j]表示s[i,j]是否为回文子串


```C++
class Solution {
public:
    string longestPalindrome(string s) {
        if(s.empty()||s.size()==1)  return s;
        int start=0, max_len=1;
        vector<vector<bool>> dp(s.size(),vector<bool>(s.size(),false));
        for(int i=0;i<s.size();++i){
            dp[i][i]=true;
            if(i>0&&s[i]==s[i-1]){
                dp[i-1][i]=true;
                start=i-1;
                max_len=2;
            }
        }
        for(int len=3;len<=s.size();++len){
            for(int i=0;i+len-1<s.size();++i){
                int j=i+len-1;
                if(s[i]==s[j]&&dp[i+1][j-1]){
                    dp[i][j]=true;
                    start=i;
                    max_len=len;
                }
            }
        }
        return s.substr(start,max_len);
    }
};
```

2. 中心拓展算法
> 回文串可以由中心拓展而来，奇数和偶数个回文串的中心分别为字符和空心，因此中心共有$2*n-1$个

```C++
class Solution {
public:
    string longestPalindrome(string s) {
        if(s.empty()||s.size()==1)  return s;
        int start=0, max_len=1;
        for(int i=0;i<s.size();++i){
            int len1=expand(s,i,i);
            int len2=expand(s,i,i+1);
            if(max(len1,len2)>max_len){
                max_len=max(len1,len2);
                start=i-(max_len-1)/2;
            }
        }
        return s.substr(start,max_len);
    }
private:
    int expand(string &s, int left, int right){
        while(left>=0&&right<s.size()&&s[left]==s[right]){
            --left;
            ++right;
        }
        return right-left-1;
    }
};
```