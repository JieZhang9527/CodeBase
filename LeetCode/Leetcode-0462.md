1. 数学运算

> 数学原理：如果移动的最终值为这个数组的中位数，则移动次数最小。如果数组个数为奇数，那么就是中位数，如果为偶数，那么中间任意一个数都可以

```C++
class Solution {
public:
    int minMoves2(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int ans=0, median=nums[nums.size()/2];
        for(auto num : nums)
            ans+=abs(num-median);
        return ans;
    }
};
```