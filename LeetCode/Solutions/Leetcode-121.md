1. 贪心
> 股票只允许买卖一次，遍历每个元素时可以减去前面的最小值，得到的就是当前点卖出能够获得的最大收益

```C++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans=0;
        int min_val=prices[0];
        for(int i=1;i<prices.size();++i){
            ans=max(ans,prices[i]-min_val);
            min_val=min(min_val,prices[i]);
        }
        return ans;
    }
};
```