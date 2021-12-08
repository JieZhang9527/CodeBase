1. dp

> dp[i]表示到[0,i]之间的最长对数链。时间复杂度很高，O(N^2)

```C++

class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        if(pairs.empty())   return 0;
        sort(pairs.begin(),pairs.end(),
            [](vector<int> a,vector<int> b){return a[1]<b[1];});
        vector<int> dp(pairs.size(),0);
        dp[0]=1;
        for(int i=1;i<pairs.size();++i){
            for(int j=0;j<i;++j){
                if(pairs[j][1]<pairs[i][0])
                    dp[i]=max(dp[i],dp[j]+1);
                else 
                    dp[i]=max(dp[i],dp[j]);
            }
        }
        return dp.back();
    }
};
```

1. 贪心算法

```C++
class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        if(pairs.empty())   return 0;
        sort(pairs.begin(),pairs.end(),[](vector<int> &a,vector<int> &b){return a[1]<b[1];});
        int ans=1;
        vector<int> end=pairs[0];
        for(auto pair : pairs){
            if(end[1]<pair[0]){
                end=pair;
                ++ans;
            }
        }
        return ans;
    }
};
```