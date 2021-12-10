1. 双指针

```C++
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int left=0, right=0;
        while(right<nums.size()){
            if(nums[left]==nums[right]) ++right;
            else{
                if(right-left==1)   return nums[left];
                else{
                    left=right;
                    ++right;
                }
            }
        }
        return nums[left];
    }
};
```

2. 二分查找

> 获取中间点是否为重复的数  
> 如果重复在左面，分别判断当前重复数的左右两侧数的个数，跳到奇数的一侧  
> 如果重复在右面，分别判断当前重复数的左右两侧数的个数，跳到奇数的一侧  

```C++
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int left=0,right=nums.size()-1;
        while(left<=right){
            int mid=left+(right-left)/2;
            if(mid-1>=0&&nums[mid-1]==nums[mid]){
                if((right-mid)%2==0)  right=mid-2;
                else left=mid+1;
            }
            else if(mid+1<nums.size()&&nums[mid+1]==nums[mid]){
                if((right-mid+1)%2==0)  right=mid-1;
                else  left=mid+2;
            }
            else
                return nums[mid];
        }
        return nums[left];
    }
};
```
