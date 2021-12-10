1. 二分查找

```C++
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left=0, right=nums.size()-1;
        while(left<=right){
            int mid=(left+right)/2;
            if(nums[mid]==target)   return mid;
            // nums[mid]在左边还是右边
            else if(nums[mid]>=nums[left]){
                // target在nums[mid]的左边还是右边
                if(target>=nums[left]&&target<nums[mid])    right=mid-1;
                else    left=mid+1;
            }
            else{
                if(target<=nums[right]&&target>nums[mid])   left=mid+1;
                else    right=mid-1;
            }
        }
        return -1;
    }
};
```