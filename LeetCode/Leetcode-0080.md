1. 双指针法
> 遍历每个值的左右边界，如果满足条件则覆盖前面的元素

```C++
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size()==0)  return 0;
        // 当前需要覆盖的元素索引
        int curr=0;
        // 相同的元素的左右边界
        int left=0, right=0;
        while(right<nums.size()){
            if(nums[left]==nums[right]){
                if(right-left+1<=2){
                    nums[curr]=nums[left];
                    ++curr;
                }
                ++right;
            }
            else{
                left=right;
            }
        }
        return curr;
    }
};
```