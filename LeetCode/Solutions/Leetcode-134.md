1. 贪心算法
> 首先,序列中的哪个位置最有可能成为出发点呢? 应该是序列中亏欠油最多的一个点的下一个点，因为从这个点出发最大限度的利用了当前拥有的油，如果消耗的大于储存的,一定不成。

```C++
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int sum=0;  // 记录每个点亏空或盈余的油量
        // 记录亏空最多的油量和相应的索引
        int min_val=INT_MAX, index=-1;
        for(int i=0;i<gas.size();++i){
            sum+=gas[i]-cost[i];
            if(sum<min_val){
                min_val=sum;
                index=i;
            }
        }
        return sum<0?-1:(index+1)%gas.size();
    }
};
```