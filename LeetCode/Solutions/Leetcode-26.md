1. 双指针法
> left和right分别记录修改后的非重复数组的尾索引和修改前数组的当前索引

```C++
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.empty())    return 0;
        int left=0, right=0;
        while(right<nums.size()){
            if(nums[left]==nums[right]) ++right;
            else{
                ++left;
                nums[left]=nums[right];
                ++right;
            }
        }
        return left+1;
    }
};
```