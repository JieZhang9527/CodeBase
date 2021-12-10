1. 遍历

```C++
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums){
        if(nums.size()<=1)  return 0;
        int max_val=INT_MIN, min_val=INT_MAX;
        int end=-1, begin=-1;
        for(int i=0;i<nums.size();++i){
            if(nums[i]<max_val) end=i;
            else    max_val=nums[i];
        }
        for(int i=nums.size()-1;i>=0;--i){
            if(nums[i]>min_val) begin=i;
            else    min_val=nums[i];
        }
        if(begin==-1&&end==-1)  return 0;
        return end-begin+1;
    }
};
```