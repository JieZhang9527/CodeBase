1. 二分查找
> 本题和33题的区别在于是否包含重复元素，可能nums[mid]=nums[left]=nums[right]，判断不出nums[mid]在左边还是右边，因此33题的策略会失效  
> 添加如下处理策略：比如11101,nums[mid]==nums[left]，++left，就会去除一种重复的干扰项

```C++
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int left=0, right=nums.size()-1;
        while(left<=right){
            int mid=(left+right)>>1;
            if(nums[mid]==target)   return true;
            else if(nums[mid]==nums[left])  ++left;
            else if(nums[mid]>nums[left]){
                if(target>=nums[left]&&target<=nums[mid])   right=mid-1;
                else left=mid+1;
            }   
            else if(nums[mid]<=nums[right]){
                if(target>=nums[mid]&&target<=nums[right])  left=mid+1;
                else    right=mid-1;
            }
        }
        return false;
    }
};
```