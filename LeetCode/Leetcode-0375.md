1. dp

>  dp(i,j) 代表在 (i,j) 中最坏情况下最小开销的代价

```C++
class Solution {
public:
    int getMoneyAmount(int n) {
        vector<vector<int>> dp(n+1,vector<int>(n+1,0));
        for(int len=2;len<=n;++len){
            for(int row=1;row+len-1<=n;++row){
                int money=INT_MAX;
                for(int col=row;col<row+len-1;++col){
                    int temp=col+max(dp[row][col-1],dp[col+1][row+len-1]);
                    money=min(money,temp);
                }
                dp[row][row+len-1]=money;
            }
        }
        return dp[1][n];
    }
};
```