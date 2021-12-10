1. 遍历
> 要保存当前最小值和最大值，因为最小值可能乘以负数变为最大值

```C++
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if(nums.empty())    return 0;
        int min_val=nums[0], max_val=nums[0];
        int ans=max_val;
        for(int i=1;i<nums.size();++i){
            int temp=max_val;   // 因为下面会改变max_val的值，因此必须暂存
            max_val=max(nums[i],max(max_val*nums[i],min_val*nums[i]));
            min_val=min(nums[i],min(temp*nums[i],min_val*nums[i]));
            ans=max(ans,max_val);
        }
        return ans;
    }
};
```