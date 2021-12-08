1. 哈希

> 注意unordered_set的删除操作

```C++
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_set<int> ust;
        for(int i=0;i<nums.size();++i){
            if(ust.find(nums[i])!=ust.end())    return true;
            ust.insert(nums[i]);
            if(ust.size()>k)    ust.erase(ust.find(nums[i-k]));
        }
        return false;
    }
};
```