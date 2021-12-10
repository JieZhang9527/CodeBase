1. 二分查找
> 二分查找找到目标值索引，左右遍历找到边界

```C++
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> ans={-1,-1};
        if(nums.empty())    return ans;   
        int left=0, right=nums.size()-1;
        int mid=-1;
        while(left<=right){
            mid=(left+right)/2;
            if(nums[mid]==target)   break;
            if(nums[mid]>target)    right=mid-1;
            else    left=mid+1;
        }
        if(mid==-1||nums[mid]!=target)   return ans;
        left=right=mid;
        while(left>=0&&nums[left]==target)  --left;
        while(right<nums.size()&&nums[right]==target)   ++right;
        ans={left+1,right-1};
        return ans;
    }
};
```