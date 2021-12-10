1. 双指针法

```C++
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        if(nums.empty())    return 0;
        int left=0, right=0;
        while(right<nums.size()){
            if(nums[right]==val)    ++right;
            else{
                nums[left]=nums[right];
                ++left;
                ++right;
            }
        }
        return left;
    }
};
```