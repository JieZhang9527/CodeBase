1. 二分查找

> 对目标值进行二分，而不是常规的索引

```C++
class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        // [left,right]是目标值的范围
        int left=0, right=0;
        for(auto num : nums){
            left=max(left,num);
            right+=num;
        }      
        while(left<right){
            int mid=left+(right-left)/2;
            int splits=split(nums,mid);
            if(splits>m)    left=mid+1;
            else    right=mid;
        }
        return left;
    }
private:
    // 按照当前子数组的最大值划分能够划分为几个部分
    int split(vector<int> &nums, int max_val){
        int splits=0, curr=0;
        for(auto num :nums){
            if(curr+num>max_val){
                curr=0;
                splits++;
            }
            curr+=num;
        }
        splits++;
        return splits;
    }
};
```