1. 双指针法

> small用于记录当前最小值，mid用于记录次小值，small和mid代表前面有这两个值，如果遇到一个更大的，说明有这三个值  
> 接下来关键是能否保证small索引在mid前面，更新顺序是先更新small,然后更新mid，也就是说mid后更新一定是在small之后

```C++
class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        if(nums.size()<3)   return false;
        int small=INT_MAX, mid=INT_MAX;
        for(auto num : nums){
            if(num<=small)   small=num;
            else if(num<=mid)    mid=num;
            else    return true;
        }
        return false;
    }
};
```