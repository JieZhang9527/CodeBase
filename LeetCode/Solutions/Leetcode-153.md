1. 二分查找
> 关键是判断出中间点在左递增序列还是右递增序列，如果在左递增序列，最小值必然在右边，如果在右递增序列，最小值在包含当前值的左边

```C++
class Solution {
public:
    int findMin(vector<int>& nums) {
        int left=0, right=nums.size()-1;
        while(left<right){
            int mid=(left+right)/2;
            if(nums[mid]<=nums[right])  right=mid;
            else    left=mid+1;
        }
        return nums[left];
    }
};
```