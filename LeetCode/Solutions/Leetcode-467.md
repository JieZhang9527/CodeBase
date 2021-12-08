1. 一次遍历

> 前提知识：字符互不相同的字符串，子串的个数为1+2+3……+n  
> 求得以每个字符结尾的最长连续子串，求和即可得到最终结果

```C++
class Solution {
public:
    int findSubstringInWraproundString(string p) {
        // 以p[i]字符结尾的最长连续子串的长度
        vector<int> dp(128,0);
        // 初始化
        dp[p[0]]=1;
        int len=1;
        for(int i=1;i<p.size();++i){
            // 更新最长连续子串的长度
            if(isContinue(p[i-1],p[i])) ++len;
            else    len=1;
            dp[p[i]]=max(dp[p[i]],len);
        }
        int ans=accumulate(dp.begin(),dp.end(),0);
        return ans;
    }
private:
    bool isContinue(char a, char b){
        return a=='z'?b=='a':b==a+1;
    }
};
```