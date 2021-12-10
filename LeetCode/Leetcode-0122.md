1. 贪心
> 注意每天既可以卖也可以买，因此可以把所有的上升势头都买了

```C++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans=0;
        for(int i=1;i<prices.size();++i)    ans+=max(0,prices[i]-prices[i-1]);
        return ans;
    }
};
```