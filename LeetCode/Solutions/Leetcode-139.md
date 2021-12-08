1. dp
> dp[i]表示str[0,i)能否由列表构成

```C++
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> ust;
        for(auto &word : wordDict)  ust.insert(word);
        vector<bool> dp(s.size()+1,false);
        dp[0]=true;
        for(int i=1;i<dp.size();++i){
            for(int j=i-1;j>=0;--j){
                dp[i]=dp[j]&&(ust.find(s.substr(j,i-j))!=ust.end());
                if(dp[i])   break;
            }
        }
        return dp.back();
    }
};
```