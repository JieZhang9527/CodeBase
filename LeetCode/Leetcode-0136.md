1. 位运算
> 异或运算满足交换律且具有如下性质: a^a=0  a^0=a

```C++
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans=0;
        for(auto num : nums)    ans^=num;
        return ans;
    }
};
```