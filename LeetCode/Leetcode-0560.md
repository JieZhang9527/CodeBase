1. 哈希

> unordered_map<int,int> mp记录数组中到当前位置的和出现的次数，假设到当前位置和为sum，那么前面出现sum-k的次数就是以当前索引为结束的和为k的子数组的个数。

```C++
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int ans=0;
        unordered_map<int,int> count;
        count.insert({0,1});
        int sum=0;
        for(int i=0;i<nums.size();++i){
            sum+=nums[i];
            if(count.find(sum-k)!=count.end())  ans+=count[sum-k];
            count[sum]++;
        }
        return ans;
    }
};
```