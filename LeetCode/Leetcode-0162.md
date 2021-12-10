1. 二分查找
> 如果nums[mid]>nums[mid+1] 峰值在左边,如果nums[mid]<nums[mid+1] 峰值在右边  
> 为什么中间值要和右边的值比较？因为计算mid时，计算的是中间偏左的，如果right-left==1

```C++
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int left=0, right=nums.size()-1;
        while(left<right){
            int mid=(left+right)/2;
            if(nums[mid]>nums[mid+1])   right=mid;
            else if(nums[mid]<nums[mid+1])  left=mid+1;
        }
        return left;
    }
};
```