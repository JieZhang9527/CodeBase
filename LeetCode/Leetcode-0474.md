1. 多维背包问题

> 经典背包问题只有一个容量，本题中有两种容量,每个物品将会占用0和1的若干个容量，产生的价值为1

> dp[i][j]表示i个0，j个1最多能拼出的字符串数目  
> 状态转移方程：dp[i][j]=max(dp[i-zeros][j-ones]+1,dp[i][j])

```C++
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        vector<vector<int>> dp(m+1,vector<int>(n+1,0));
        for(auto &str : strs){
            int zeros=0, ones=0;
            help(str,zeros,ones);
            for(int i=m;i>=zeros;--i){
                for(int j=n;j>=ones;--j){
                    dp[i][j]=max(dp[i-zeros][j-ones]+1,dp[i][j]);
                }
            }
        }
        return dp[m][n];
    }
private:
    void help(const string &str, int &zeros, int &ones){
        for(auto c : str)
            c=='0'?++zeros:++ones;
    }
};
```