1. 二分查找

```C++
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left=0,right=nums.size()-1,mid;
        while(left<=right){
            mid=(left+right)/2;
            if(nums[mid]==target) return mid;
            else if(nums[mid]<target) left=mid+1;
            else  right=mid-1;
        }
        if(target>nums[mid])  return mid+1;
        else  return mid;
    }
};
```