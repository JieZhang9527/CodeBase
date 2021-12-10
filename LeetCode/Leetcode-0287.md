1. 二分查找

```C++
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int left=0, right=nums.size()-1;
        while(left<right){
            int mid=(left+right)/2;
            int count=0;
            // 数组未排序，必须全部遍历
            for(auto num : nums){
                if(num<=mid)    ++count;
            }
            // mid太小，小的在前面
            if(count>mid)   right=mid;
            else    left=mid+1;
        }
        return left;
    }
};
```