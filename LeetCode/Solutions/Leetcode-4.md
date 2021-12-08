1. 暴力排序
> 新建nums数组，排序后获取中位数

```C++
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> nums=nums1;
        nums.insert(nums.end(),nums2.begin(),nums2.end());
        sort(nums.begin(),nums.end());
        int mid=nums.size()>>1;
        return nums.size()%2?nums[mid]:(nums[mid]+nums[mid-1])/2.0;
    }
};
```

2. 双指针排序
> 暴力排序未能有效利用两个数组各自有序的特点

```C++
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> nums;
        int index1=0, index2=0;
        while(index1<nums1.size()&&index2<nums2.size()){
            if(nums1[index1]<nums2[index2]){
                nums.push_back(nums1[index1]);
                ++index1;
            }
            else{
                nums.push_back(nums2[index2]);
                ++index2;
            }
        }
        while(index1<nums1.size())  nums.push_back(nums1[index1++]);
        while(index2<nums2.size())  nums.push_back(nums2[index2++]);
        int mid=nums.size()>>1;
        return nums.size()%2?nums[mid]:(nums[mid-1]+nums[mid])/2.0;
    }
};
```