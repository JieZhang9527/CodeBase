1. dp
> dp[i]表示字符串[0,i]的最小分割次数

```C++
class Solution {
public:
    int minCut(string s) {
        if(s.size()<2)  return 0;
        vector<int> dp(s.size(),0);
        for(int i=0;i<s.size();++i) dp[i]=i;
        for(int i=1;i<s.size();++i){
            if(help(s,0,i)){
                dp[i]=0;
                continue;
            }
            for(int j=0;j<i;++j){
                if(help(s,j+1,i))   dp[i]=min(dp[i],dp[j]+1);
            }
        }
        return dp.back();
    }
private:
    // 判断是否为回文串
    bool help(string &str, int left, int right){
        while(left<right){
            if(str[left]!=str[right])   return false;
            ++left;
            --right;
        }
        return true;
    }
};
```