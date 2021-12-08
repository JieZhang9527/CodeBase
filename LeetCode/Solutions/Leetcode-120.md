1. dp
> 自底向上求解，dp[i]表示从底层到达该层的第i个节点的最小距离，如果自顶向下求解，则数组需要动态扩展，判断条件较为复杂

```C++
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        if(triangle.empty())    return 0;
        vector<int> dp(triangle.size()+1,0);
        for(int i=triangle.size()-1;i>=0;--i){
            for(int j=0;j<=i;++j){
                dp[j]=min(dp[j],dp[j+1])+triangle[i][j];
            }
        }
        return dp[0];
    }
};
```