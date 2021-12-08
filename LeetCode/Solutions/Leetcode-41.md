1. 原地哈希

```C++
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        if(nums.empty())    return 1;
        for(int i=0;i<nums.size();++i){
            while(nums[i]>=0&&nums[i]<nums.size()&&nums[i]!=nums[nums[i]])
                swap(nums[i],nums[nums[i]]);
        }
        for(int i=1;i<nums.size();++i){
            if(nums[i]!=i)  return i;
        }
        // [*, 1, 2, 3, 4]
        return nums[0]==nums.size()?nums.size()+1:nums.size();
    }
};
```